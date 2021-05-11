from random import randint


class BankAccount():
    # Properties
    __account_number = ''
    owner = ''
    __balance = 0

    # Constructor
    def __init__(self, owner):
        self.__generate_account_number()
        self.owner = owner

    # Getters / Setters
    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # Commented getters / setters regular way without decorators
    # def get_account_number(self):
    #     return self.__account_number
    #
    # def get_balance(self):
    #     return self.__balance

    # Commented method because I don't want to give write permissions
    # def set_account_number(self, account_number):
    #     self.__account_number = account_number

    # Methods
    def __generate_account_number(self):
        self.__account_number = randint(0, 999)

    def add_money(self, money):
        if money > 0:
            self.__balance += money

    def take_money(self, money):
        if money > 0:
            self.__balance -= money


account = BankAccount('Cristina')
print(account.account_number)
print(account.balance)
account.balance = 500
print(account.balance)
# print(account.balance)
# account.add_money(500)
# print(account.balance)
# account.take_money(200)
# print(account.balance)
# print(account.get_account_number())
# print(account.get_balance())
# account.add_money(500)
# print(account.get_balance())
# account.take_money(200)
# print(account.get_balance())
# account.set_account_number(100)