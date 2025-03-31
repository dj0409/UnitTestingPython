import logging

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_interest_rate():
    """
    In a real-world scenario, this might fetch the current interest rate from an external service.
    Here we simply return a constant value for demonstration purposes.
    """
    return 0.01  # 1% interest rate

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        logger.info(f"{self.owner} deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        logger.info(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
    
    def apply_interest(self):
        """
        Applies interest to the current balance using the interest rate provided by get_interest_rate.
        Returns the interest amount.
        """
        interest_rate = get_interest_rate()
        interest = self.balance * interest_rate
        self.balance += interest
        logger.info(f"{self.owner} received interest {interest} at rate {interest_rate}. New balance: {self.balance}")
        return interest

def transfer_funds(from_account, to_account, amount):
    """
    Transfers funds from one account to another.
    Raises a ValueError if the transfer amount is not positive.
    """
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")
    from_account.withdraw(amount)
    to_account.deposit(amount)
    logger.info(f"Transferred {amount} from {from_account.owner} to {to_account.owner}")

