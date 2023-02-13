 
import unittest
from bank import BankAccount
from metro import User, Admin
from metro import ChargebleTicket, ExpirableTicket, DisposableTicket
from exceptions import *

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(username="user", password="password#")
        self.admin = Admin(username="admin", password="password#")

    def test_validate_username(self):
        with self.assertRaises(DuplicateUsernameError):
            User(username="user", password="password#2321")
            User(username="user", password="password#2321")
        with self.assertRaises(AssertionError):
            User(username="user", password="short")

    def test_validate_password(self):
        with self.assertRaises(SpecialCharError):
            User(username="username", password="nopunctuation")
        with self.assertRaises(AssertionError):
            User(username="username", password="tooshort")

    def test_make_deposit(self):
        self.user.make_deposit(10)
        self.assertEqual(self.user.account.balance, 20)

    def test_make_withdraw(self):
        self.user.make_withdraw(5)
        self.assertEqual(self.user.account.balance, 5)

    def test_buy_ticket(self):
        ticket = "ticket"
        self.user.buy_ticket(ticket)
        self.assertEqual(self.user.ticket_list[0], ticket)

    def test_show_ticket_list(self):
        ticket = "ticket"
        self.user.buy_ticket(ticket)
        self.assertEqual(self.user.show_ticket_list(), [ticket])
        self.assertEqual(self.user.show_ticket_list(0), ticket)

    def test_update_user(self):
        self.user.update_user()
        self.assertTrue(os.path.exists(f"users/{self.user.id}.pickle"))

    def test_save_user(self):
        self.user.save_user()
        self.assertTrue(os.path.exists(f"users/{self.user.id}.pickle"))
