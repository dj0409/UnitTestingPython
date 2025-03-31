# test_app.py

import pytest
from app import User

@pytest.fixture
def user():
    """Fixture that returns a User object with an initial balance of 100."""
    return User(username="batman", balance=100)

def test_deposit(user):
    # Test deposit functionality
    user.deposit(50)
    assert user.get_balance() == 150

def test_withdraw(user):
    # Test withdraw functionality
    user.withdraw(30)
    assert user.get_balance() == 70

def test_insufficient_balance(user):
    # Test that withdrawing more than the balance raises an error
    with pytest.raises(ValueError, match="Insufficient balance"):
        user.withdraw(200)

def test_negative_deposit(user):
    # Test that depositing a negative amount raises an error
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        user.deposit(-10)

def test_negative_withdraw(user):
    # Test that withdrawing a negative amount raises an error
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        user.withdraw(-20)
