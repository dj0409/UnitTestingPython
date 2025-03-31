import pytest
from bank import BankAccount, transfer_funds, get_interest_rate
from unittest.mock import patch

# --- Simple Test Cases ---

def test_deposit():
    """ Checks if the deposit is succesful"""
    account = BankAccount("Alice", 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = BankAccount("Bob", 200)
    account.withdraw(50)
    assert account.balance == 150

def test_withdraw_insufficient_funds():
    account = BankAccount("Charlie", 100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)

def test_deposit_negative_amount():
    account = BankAccount("Alice", 100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-10)

# --- Parameterized Tests ---

@pytest.mark.parametrize("initial, deposit, expected", [
    (100, 50, 150),
    (200, 100, 300),
    (0, 25, 25),
])
def test_parameterized_deposit(initial, deposit, expected):
    account = BankAccount("Test", initial)
    account.deposit(deposit)
    assert account.balance == expected

# --- Test for Transfer Funds ---

def test_transfer_funds():
    account1 = BankAccount("Alice", 100)
    account2 = BankAccount("Bob", 50)
    transfer_funds(account1, account2, 70)
    assert account1.balance == 30
    assert account2.balance == 120

def test_transfer_negative_amount():
    account1 = BankAccount("Alice", 100)
    account2 = BankAccount("Bob", 50)
    with pytest.raises(ValueError, match="Transfer amount must be positive"):
        transfer_funds(account1, account2, -20)

# --- Testing apply_interest with Mocking ---

def test_apply_interest():
    account = BankAccount("Dave", 1000)
    # Patch get_interest_rate to simulate a 5% interest rate.
    with patch("bank.get_interest_rate", return_value=0.05):
        interest = account.apply_interest()
    expected_interest = 1000 * 0.05
    assert interest == expected_interest
    assert account.balance == 1000 + expected_interest

# --- Testing Logging using PyTest's caplog Fixture ---

def test_logging_on_deposit(caplog):
    account = BankAccount("Alice", 100)
    with caplog.at_level("INFO"):
        account.deposit(50)
    # Check that the log contains a message about the deposit.
    assert any("Alice deposited 50" in record.message for record in caplog.records)
