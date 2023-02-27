import pickle
import glob
import json
import logging
import os
from pprint import pprint
from metro import Admin, User, clear, ChargebleTicket, ExpirableTicket, DisposableTicket
from exceptions import *


menu = '''
__  __      _
|  \/  | ___| |_ _ __ ___
| |\/| |/ _ \ __| '__/ _ \

| |  | |  __/ |_| | | (_) |
|_|  |_|\___|\__|_|  \___/'''

admin_pyfig = '''
    _    ____  __  __ ___ _   _
   / \  |  _ \|  \/  |_ _| \ | |
  / _ \ | | | | |\/| || ||  \| |
 / ___ \| |_| | |  | || || |\  |
/_/   \_\____/|_|  |_|___|_| \_|
'''

logging.basicConfig(filename='Logs/metro.log', level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(message)s %(module)s')

logger = logging.getLogger(__name__)
error_logger = logging.getLogger('error_logger')
error_f_h = logging.FileHandler('Logs/errors.log')
error_f_f = logging.Formatter('%(asctime)s - %(message)s %(name)s %(message)s %(module)s')
error_f_h.setFormatter(error_f_f)
error_logger.addHandler(error_f_h)


def terminal_dictionary_display(dictionary : dict):
    print(json.dumps(dictionary, indent=4))


def show_ticket(person, generator):
    temp = []
    for i in enumerate(person.show_ticket_list(), 1):
        temp.append(i)
    return temp


class Menu:
    login_menu = {
        '1': 'Bank Account Manager',
        '2': 'Buy Ticket',
        '3': 'Take a Trip',
        '4': 'Logout'}

    bank_acount_menu = {
        '1': 'Deposit',
        '2': 'Withdraw',
        '3': 'Your Balance',
        '4': 'return...'}

    buy_ticket_menu = {
        '1': 'Chargeable',
        '2': 'Disposable(you can use it only once)',
        '3': 'Date Expirable',
        '4': 'Show Ticket List',
        '5': 'Charge Chargeable card'}

    admin_menu = {
        '1': 'CREATE NEW ADMIN',
        '2': 'BAN USER',
        '3': 'TICKET EDIT TOOLS',
        '4': 'Logout'
    }

    admin_ticket = {
        '1': 'CREATE TICKET',
        '2': 'EDIT TICKETS',
        '3': 'DELETE TICKET'
    }

    @staticmethod
    def extract_pickle_files(list_of_objs: list, file_path):
        for file in glob.glob(f"{file_path}/*.pickle"):
            with open(file, 'rb') as obj:
                while True:
                    try:
                        content = pickle.load(obj)
                        list_of_objs.append(content)
                    except (EOFError, ModuleNotFoundError) as e:
                        error_logger.error(e)
                        break
        return list_of_objs

    @classmethod
    def find_user_by_username(cls, name: str, search_path: str):
        results = []
        for root, dirname, files in os.walk(search_path):
            # print(f'{files}')
            for filename in files:
                try:
                    with open(f"{search_path}/{filename}", 'rb') as user:
                        if name == pickle.load(user).username:
                            return True
                except Exception as e:
                    print(e)
        return False

    @staticmethod
    def run():
        while True:
            clear()
            print(menu)
            print('\nSelect one of the below')
            user_options = {
                '1': 'Registeration',
                '2': 'Log in (User)',
                '3': 'Log in (SuperUser)',
                '4': 'Exit'
            }

            terminal_dictionary_display(user_options)

            user_input_menu = input('Choose: ')
            # REGISTER MENU

            if user_input_menu == '1':
                clear()
                name = input('Enter username: ').strip()
                try:
                    if Menu.find_user_by_username(name, search_path='users'):
                        raise DuplicateUsernameError("Duplicate Username")
                    password = input('Enter password: ')
                    user_obj = User(name, password)
                    user_obj.save_user()
                    print(f'You Are Now Part of METRO\nYour Metro ID: {user_obj.id}')

                except DuplicateUsernameError as e:
                    error_logger.error(e)
                    print(e)
                except AssertionError as e:
                    error_logger.error(e)
                    print(e)
                except SpecialCharError as s:
                    error_logger.error(s)
                    print(s)
                input('C...')
            # LOGIN FORGET PASSWORD

            elif user_input_menu == '2':
                clear()
                user_id = input('Enter Unique ID(Forgot password?(y)): ')
                log_in_flag = False
                objects = []
                if user_id == 'y':
                    clear()
                    Menu.extract_pickle_files(objects, "users")
                    name = input('Enter username: ')
                    password = input('Enter password: ')
                    for user in objects:
                        if user.username == name and user.password == password:
                            print(f'Your id is:\n{user.id}')
                            input('Continue...')
                            clear()
                            break
                    else:
                        print("Wrong Password or username")
                        input('Continue...')

                # LOGIN
                else:
                    try:
                        with open(f"users/{user_id}.pickle", 'rb') as user:
                            logged_in_person = pickle.load(user)
                        log_in_flag = True
                        logger.info("%s has successfuly logged in", logged_in_person.username)
                        if logged_in_person.banned_user:
                            log_in_flag = False
                            input("You have been banned from metro\nvisit this link to get more information/\ncontact admin at Admin@admin.mail to remove ban")

                    except FileNotFoundError:
                        logger.error("User not found!")
                        print("User Not Found!")
                        input('C..')
                # input(logged_in_person.banned_user)

                # LOGIN MENU
                while log_in_flag:
                    clear()
                    terminal_dictionary_display(Menu.login_menu)
                    login_user_input = input("What do you desire? ")
                    # BANK ACCOUNT MENU
                    if login_user_input == '1':
                        clear()
                        terminal_dictionary_display(Menu.bank_acount_menu)
                        user_input = input("Choose: ")
                        # DEPOSIT
                        if user_input == '1':
                            clear()
                            amount = input('The amount you want to deposit? ')
                            input('Shaparak')
                            logged_in_person.make_deposit(float(amount))
                            print(logged_in_person.account.balance)
                            input('C...')
                            logger.info("%s has successfuly deposited %s", logged_in_person.username, amount)

                        # WITHDRAW
                        elif user_input == '2':
                            clear()
                            amount = input('The amount you want to Withdraw? ')
                            input('Shaparak')
                            try:
                                logged_in_person.make_withdraw(float(amount))
                                print(logged_in_person.account.balance)
                                logger.info("%s has successfuly withdrew %s", logged_in_person.username, amount)
                                input('C...')
                            except AssertionError as e:
                                print(e)
                                error_logger.error(e)
                                input()

                        # SHOW BALANCE
                        elif user_input == '3':
                            clear()
                            try:
                                print(logged_in_person.account.display_account_info(logged_in_person.username))
                                input('C...')
                            except AssertionError as e:
                                print(e)
                                logger.error(e)
                                input('C...')

                    # BUY TICKET
                    elif login_user_input == '2':
                        clear()
                        terminal_dictionary_display(Menu.buy_ticket_menu)
                        user_ticket_choice = input('choose: ')
                        # BUY CHARGEBLE TICKET
                        c_flag = False
                        if user_ticket_choice == '1':
                            command = "ChargebleTicket()"
                        elif user_ticket_choice == '2':
                            command = "DisposableTicket()"
                        elif user_ticket_choice == '3':
                            command = "ExpirableTicket()"
                        elif user_ticket_choice == '4':
                            clear()
                            for i in enumerate(logged_in_person.show_ticket_list(), 1):
                                print(i, '\n')  # indent=2)
                            c_flag = True
                            input('C...')

                        # CHARGE TICKET
                        elif user_ticket_choice == '5':
                            temp = []
                            for ticket in enumerate(logged_in_person.show_ticket_list(), 1):
                                if isinstance(ticket[1], ChargebleTicket):
                                    pprint(ticket, indent=1)
                                    temp.append(ticket)
                            charging = int(input('which card would you like to chrage? '))
                            amount = int(input('How much you want to charge your card?\n1.20\n2.30\n3.40\n'))
                            list_of_prices = [20, 30, 40]
                            try:
                                logged_in_person.make_withdraw(list_of_prices[amount - 1])
                                logged_in_person.charge_chargeble_ticket(charging, list_of_prices[amount - 1])
                            except AssertionError as e:
                                error_logger.error(e)
                                print(e)
                                input()
                            print(logged_in_person.ticket_list)
                            c_flag = True
                            input()
                        else:
                            input('Invalid Input...')

                        if not c_flag:
                            try:
                                logged_in_person.make_withdraw(55)
                                ticket_obj = eval(command)
                                logged_in_person.buy_ticket(ticket_obj)
                                print(logged_in_person.ticket_list[-1])
                                logger.info("%s bought %s", logged_in_person.username, type(ticket_obj).__name__)
                                input("C...")

                            except AssertionError as k:
                                print(k)
                                error_logger.error(k)
                                input()

                    # MAKING A TRIP
                    elif login_user_input == '3':
                        clear()
                        for i in enumerate(logged_in_person.show_ticket_list(), 1):
                            print(i, '\n')
                        chosen_ticket = input('Which ticket would you like to use for this Trip? ')

                        try:
                            if len(chosen_ticket) == 1 and chosen_ticket.isdigit():
                                logged_in_person.use_ticket_bynumber(int(chosen_ticket))
                            elif len(chosen_ticket) > 1:
                                logged_in_person.use_ticket_byid(chosen_ticket)
                            logger.info("%s has taken a trip", logged_in_person.username)
                            # logged_in_person.ticket_list[int(chosen_ticket) - 1].use_ticket()
                            print(logged_in_person.ticket_list)
                            input('Ticket has been used successfuly...')
                            # logged_in_person.make_trip('')
                            input('You can now travel using metro...')
                        except AssertionError as e:
                            print(e)
                            error_logger.error(e)
                            input('C...')

                    elif login_user_input == '4':
                        logged_in_person.save_user()
                        logger.info("%s logged out", logged_in_person.username)
                        break

            elif user_input_menu == '3':
                clear()
                a = ''' With Great power comes great responsibility'''
                b = len(a) * '_'
                print(f"\t{b}\n\n\t{a}\n\t{b}\n")
                admin_username = input('\tEnter username: ')
                admin_password = input('\tEnter password: ')
                admin_objs = []
                Menu.extract_pickle_files(admin_objs, "admins")
                logged_in_admin = False
                the_admin = object
                for admin in admin_objs:
                    if admin.username == admin_username and admin.password == admin_password:
                        logged_in_admin = True
                        the_admin = admin
                        logger.info("admin tried to log in")

                if not logged_in_admin:
                    clear()
                    print("Are you on drugs?")
                    input('C...')
                    continue

                while True:
                    if logged_in_admin:
                        clear()
                        print(admin_pyfig)
                        terminal_dictionary_display(Menu.admin_menu)
                        admin_input = input('Choose: ')

                        if admin_input == '1':
                            clear()
                            name = input('Enter username: ')
                            password = input('Enter password: ')
                            admin_obj = Admin(name, password)
                            admin_obj.save_user()
                            print('You Are Now METRO Admin')
                            print(f'Your Metro ID: {admin_obj.id}')
                            input('C...')
                        # BAN USER
                        if admin_input == '2':
                            clear()
                            user_id = input("user ID to ban: ")
                            filename = f'{user_id}.pickle'
                            try:
                                user = the_admin.find_user(filename, './users')
                                print(user, '\n')
                                x = input("Are you sure?(y/n)")
                                authentication = True if x == 'y' else False
                                print(authentication)
                                if authentication is True:
                                    the_admin.ban_user(user)
                                    print("User banned successfuly!")
                                    input()
                                else:
                                    input()
                            except IndexError as e:
                                print("no User found!")
                                input()
                            user.save_user()



                        # CREATE TICKET
                        elif admin_input == '3':
                            clear()
                            terminal_dictionary_display(Menu.admin_ticket)
                            aticket_input = input('Choose: ')

                            if aticket_input == '1':
                                ticket_kind = int(input("What kind of ticket do you want me to create?\n1. chargeble\n2. expirable\n3. disposable\n"))
                                if ticket_kind == 1:
                                    the_admin.make_ticket(ChargebleTicket())
                                    print('1', show_ticket(the_admin, the_admin.show_ticket_list()))
                                    try:
                                        print(the_admin.show_ticket_list(1))

                                    except IndexError as e:
                                        print(e)
                                    input()
                                elif ticket_kind == 3:
                                    the_admin.make_ticket(DisposableTicket())
                                    print(the_admin.ticket_list[-1])
                                elif ticket_kind == 2:
                                    the_admin.make_ticket(ExpirableTicket())
                                    print(the_admin.ticket_list[-1])
                            elif aticket_input == '2':
                                print("Do you want to search by ID?")
                                os.chdir("tickets")
                                clear()
                                ticket_id = input("user ID to ban: ")
                                filename = f'{user_id}.pickle'
                                ticket = the_admin.find_ticket(filename, './tickets')
                                print(ticket, '\n')
                                x = input("Are you sure?(y/n)")
                                authentication = True if x == 'y' else False
                                if authentication is True:
                                    the_admin.ban_user(user)
                                    input()

                            elif aticket_input == '3':
                                clear()
                                ticket_id = input('Enter ticket ID: ')
                                os.chdir('tickets')
                                os.system(f'del {ticket_id}.pickle' if os.name == 'nt' else f"rm {ticket_id}.pickle")
                                input()

                        elif admin_input == '4':
                            the_admin.update_admin()
                            break

            elif user_input_menu == '4':
                break


if __name__ == '__main__':
    Menu.run()

# 36fbcdb6-a6fe-11ed-a7c4-a41731ccaf53
