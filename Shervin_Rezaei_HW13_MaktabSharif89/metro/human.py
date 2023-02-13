import logging
import pickle
import os
import uuid
import glob
from bank import BankAccount
from exceptions import *
#
admin_logger = logging.getLogger('Admin_logger')
admin_logger.setLevel(logging.INFO)
admin_f_h = logging.FileHandler('Admins.log')
admin_f_f = logging.Formatter('%(asctime)s - %(message)s')
admin_f_h.setFormatter(admin_f_f)
admin_f_h.setLevel(level=logging.INFO)
admin_logger.addHandler(admin_f_h)



class User:

    username_list = []

    def __init__(self, username, password):
        self._validate_username(username)
        self._validate_password(password)
        self.username = username
        self.__password = password
        self.account = BankAccount(title="Main_Account", balance=10)
        self.ticket_list = []
        self.__id = uuid.uuid1()
        self.banned_user = False

        logging.info('User instance created: name=%s, id=%r', self.username, self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newpass):
        self.validate_password(newpass)
        self.__password = newpass

    def reset_password(self):
        npass = self.security()
        if npass:
            self._password = npass

    def _validate_username(self, user):
        assert 4 <= len(user) <= 8, 'Length must be between 4 and 8'
        assert user not in self.__class__.username_list, DuplicateUsernameError("This username is already taken")
        return user

    @staticmethod
    def _validate_password(_npass):
        special = ('#', '@', '&', '?', '!', '*', '$')
        assert 8 <= len(_npass) <= 16, 'Password length must be between 8 and 16'
        #assert npass.isalnum(), ValueError('must contain character and digits')
        assert (not _npass.isalpha() and not _npass.isdigit()), 'must contain character and digits'
        assert [i for i in _npass if i in special], SpecialCharError('Must contain special charachter')

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_account_info(self):
        self.account.display_account_info(self.username)
        return self

    def buy_ticket(self, ticket):
        self.ticket_list.append(ticket)

    def make_trip(self, location):
        pass

    def use_ticket_bynumber(self, ticket):
        self.ticket_list[ticket - 1].use_ticket()
        self.ticket_validation(self.ticket_list[ticket - 1])

    def use_ticket_byid(self, ticket_id):
        for ticket in self.ticket_list:
            # print(ticket)
            if ticket_id == str(ticket.ticket_id):
                ticket.use_ticket()
                self.ticket_validation(ticket)

    def charge_chargeble_ticket(self, number, amount):
        self.ticket_list[number - 1].charge_ticket(amount)

    def ticket_validation(self, ticket):
        if ticket.check_expiration():
            self.ticket_list.remove(ticket)

    def show_ticket_list(self, index=None):
        if index:
            return self.ticket_list[index]
        return self.ticket_list

    def update_admin(self):
        with open(f"admins/{self.id}.pickle", 'wb') as user:
            pickle.dump(self, user)

    def save_user(self):
        with open(f"users/{self.id}.pickle", 'wb') as user:
            pickle.dump(self, user)

    def __repr__(self):
        return f"""\n\tusername:{self.username}\n\tuser_id:{self.__id}"""


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        admin_logger.info("%s created", self.username)

    def create_new_admin(self):
        pass

    def make_ticket(self, ticket):
        self.ticket_list.append(ticket)
        admin_logger.info("%s created", ticket)

    def find_user(self, filename, search_path):
        result = []
        for root, dirname, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        with open(f'{result[0]}', 'rb') as f:
            user = pickle.load(f)
        return user

    def find_user_by_username(self, filename, search_path):
        results = []
        for root, dirname, files in os.walk(search_path):
            print(f'{root}\n{dirname}\n{files}')
            try:
                with open(files, 'rb') as user:
                    results.append(pickle.load(user).username)
                    print(results)
            except Exception:
                return True

    def find_ticket(self, filename, search_path):
        result = []
        for root, dirname, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        with open(f'{result[0]}', 'rb') as f:
            ticket = pickle.load(f)
        return ticket

    def save_user(self, path="admins"):
        with open(f"{path}/{self.id}.pickle", 'wb') as user:
            pickle.dump(self, user)

    def ban_user(self, user : User):
        user.banned_user = True
        admin_logger.info("%s banned user", user.username)
        # self.__class__.ticket_list.append()

    def delete_ticket_by_id(self, ticket_id):
        os.chdir('tickets')
        os.system(f'del {ticket_id}.pickle' if os.name =='nt' else f"rm {ticket_id}.pickle")
        admin_logger.info("%s ticket deleted", ticket_id)
        input()


#
# obj = Admin('admin', 'admin')
# obj.save_user(path='.')
