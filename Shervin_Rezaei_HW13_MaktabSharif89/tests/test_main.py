
import unittest
from typing import BinaryIO
import pickle
import glob
from bank import BankAccount
from metro import ChargebleTicket, ExpirableTicket, DisposableTicket, User, Admin


class TestMenu(unittest.TestCase):
    def test_create_new_user(self):
        user_obj = User("TestUser", "passsw#3434")
        user: BinaryIO
        with open(f"users/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        with open(f"users/{user_obj.id}.pickle", 'rb') as user:
            loaded_user = pickle.load(user)

        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.username, "TestUser")
        self.assertEqual(loaded_user.password, "passsw#3434")

    def test_log_in_as_admin(self):
        admin_obj = Admin("TestAdmin", "TestPassword")
        with open(f"C:/Users/DearUser/Desktop/metro-gp/admin/{admin_obj.id}.pickle" , 'wb') as admin:
            pickle.dump(admin_obj, admin)

        objects = []
        for file in glob.glob("C:/Users/DearUser/Desktop/metro-gp/admin/*.pickle"):
            with open(file, 'rb') as admin:
                while True:
                    try:
                        content = pickle.load(admin)
                        objects.append(content)
                    except EOFError:
                        break

        for admin in objects:
            if admin.username == "TestAdmin":
                if admin.password == "TestPassword":
                    logged_in_admin = admin
                    break
        self.assertIsInstance(logged_in_admin, Admin)
        self.assertEqual(logged_in_admin.username, "TestAdmin")
        self.assertEqual(logged_in_admin.password, "TestPassword")
    def test_log_in_as_user(self):
        user_obj = User("TestUser", "TestPassword")
        with open(f"users/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        objects = []
        for file in glob.glob("users/*.pickle"):
            with open(file, 'rb') as user:
                while True:
                    try:
                        content = pickle.load(user)
                        objects.append(content)
                    except EOFError:
                        break

        for user in objects:
            if user.username == "TestUser":
                if user.password == "TestPassword":
                    logged_in_user = user
                    break

        self.assertEqual(logged_in_user.username, "TestUser")
        self.assertEqual(logged_in_user.password, "TestPassword")
    def test_deposit(self):
        user_obj = User("TestUser", "TestPassword")
        with open(f"users/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)
        with open(f"users/{user_obj.id}.pickle", "rb") as user:
            user_obj = pickle.load(user)

        initial_balance = user_obj.balance
        deposit_amount = 100
        user_obj.deposit(deposit_amount)

        with open(f"users/{user_obj.id}.pickle", "rb") as user:
            user_obj = pickle.load(user)

        self.assertEqual(user_obj.balance, initial_balance + deposit_amount)

    def test_withdraw(self):
        user_obj = User("TestUser", "TestPassword")
        user_obj.deposit(100)
        with open(f"users/{user_obj.id}.pickle" , 'wb') as user:
            pickle.dump(user_obj, user)

        user_obj.withdraw(50)
        with open(f"users/{user_obj.id}.pickle" , 'rb') as user:
            loaded_obj = pickle.load(user)

        self.assertEqual(loaded_obj.balance, 50)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.user = User("test_user", "password")
        with open(f"users/{self.user.id}.pickle" , 'wb') as user:
            pickle.dump(self.user, user)

    def test_run(self):
        self.assertIsNotNone(self.menu.run())

    def test_register_user(self):
        user_id = self.user.id
        with open(f"users/{user_id}.pickle", 'rb') as user:
            user_obj = pickle.load(user)

        self.assertEqual(user_obj.username, "test_user")
        self.assertEqual(user_obj.password, "password")

    def tearDown(self):
        os.remove(f"users/{self.user.id}.pickle")

