import unittest
from BankAccount import Customer, BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.akbar = Customer('Akbar', 'Babaii', '09123456789', 'akbar@gmail.com')
        self.asqar = Customer('Asqar', 'Rezaii', '09123456788', 'asqar@gmail.com')
        self.akbar_account = BankAccount(self.akbar, 50000)
        self.asqar_account = BankAccount(self.asqar, 10000)

    def test_withdraw(self):
        self.akbar_account.withdraw(1000)
        self.assertEqual(49000 - 2*(BankAccount.WAGE_AMOUNT) , self.akbar_account.get_balance(), "did not work")

    def test_deposit(self):
        self.asqar_account.deposit(1000)
        self.assertEqual(11000 - BankAccount.WAGE_AMOUNT, self.asqar_account.get_balance())

    def test_get_balance(self):
        self.assertEqual(10000 - BankAccount.WAGE_AMOUNT, self.asqar_account.get_balance())

    def test_transfer(self):
        self.akbar_account.transfer(self.asqar_account, 1000)
        self.assertEqual(49000 - 2 * (BankAccount.WAGE_AMOUNT), self.akbar_account.get_balance())
        self.assertEqual(11000 - BankAccount.WAGE_AMOUNT, self.asqar_account.get_balance())

    def test_change_wage(self):
        BankAccount.change_wage(100)
        # print(BankAccount.WAGE_AMOUNT)
        self.assertEqual(100, BankAccount.WAGE_AMOUNT)

    def test_change_min_balance(self):
        pass




if __name__ == "__main__":
    unittest.main()
