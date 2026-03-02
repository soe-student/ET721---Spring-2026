import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):
    """Unit tests for the BankAccount class."""
    
    def setUp(self):
        """Create a default BankAccount instance before each test."""
        self.account = BankAccount(owner="Test User", balance=100.0)
    
    def test_initial_balance(self):
        """Test that the account is initialized with the correct balance."""
        self.assertEqual(self.account.get_balance(), 100.0)
        
    def test_deposit(self):
        """Test that a deposit operation correctly adds to the balance."""
        self.account.deposit(50.0)
        self.assertEqual(self.account.get_balance(), 150.0)
        
    def test_withdrawal(self):
        """Test that a withdrawal operation correctly subtracts from the balance."""
        self.account.withdraw(30.0)
        self.assertEqual(self.account.get_balance(), 70.0)
        
    def test_withdraw_more_than_balance(self):
        """Test that withdrawing more than available balance raises ValueError."""
        with self.assertRaises(ValueError):
            self.account.withdraw(150.0)
    
    def test_sequence_of_operations(self):
        """Test a sequence of deposits and withdrawals for correct balance."""
        # Initial balance: 100.0
        self.account.deposit(50.0)  # Balance: 150.0
        self.assertEqual(self.account.get_balance(), 150.0)
        
        self.account.withdraw(30.0)  # Balance: 120.0
        self.assertEqual(self.account.get_balance(), 120.0)
        
        self.account.deposit(25.0)  # Balance: 145.0
        self.assertEqual(self.account.get_balance(), 145.0)
        
        self.account.withdraw(45.0)  # Balance: 100.0
        self.assertEqual(self.account.get_balance(), 100.0)
        
        # Final balance should be 100.0
        self.assertEqual(self.account.get_balance(), 100.0)


if __name__ == '__main__':
    unittest.main()