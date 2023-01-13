from models import Product, User
from datetime import datetime


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if amount > self.products.get(product):
            raise ValueError('Not Enough Products')
        else:
            self.products[product] = self.products.get(product, 0) - amount

        if self.products.get(product) == 0:
            self.products.pop(product)

    def add_user(self, username):
        for user in self.users:
            if username == user.username:
                return None
            user = User(username)
            self.users.append(User(user))
            return username

    def get_total_asset(self):
        amount = []
        price = []
        sum = 0
        for product, quant in self.products.items():
            amount.append(quant)
            price.append(product.price)
        for i in range(len(amount)):
            result = amount[i] * price[i]
            sum += result
        return sum

    def get_total_profit(self):
        sum = 0
        for user in self.users:
            for product in user.bought_products:
                sum += product.price
        return sum

    def get_comments_by_user(self, user):
        list_of_comments_by_user = []
        for p in self.products.keys():
            for comment in p.comments:
                if comment.user == user:
                    list_of_comments_by_user.append(comment.text)
        return list_of_comments_by_user

    def get_inflation_affected_product_names(self):
        name = None
        price = 0
        iap = []
        for product in self.products.keys():
            if product.name == name or name is None:
                if product.price != price and price != 0:
                    iap.append(product.name)
                price = product.price
                name = product.name
        name2 = ''
        for i in iap:
            if i == name2:
                iap.remove(i)
            name2 = i
        return iap

    def clean_old_comments(self, date):
        for product in self.products:
            product.comments = [comment for comment in product.comments if comment.date_added > datetime.strptime(date, '%Y-%m-%d')]

    def get_comments_by_bought_users(self, product):
        list_of_comments =[]
        for username in self.users:
            for p in username.bought_products:
                if product == p:
                    for comment in p.comments:
                        if comment.user == username:
                            list_of_comments.append(comment.text)

        return list_of_comments



