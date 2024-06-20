# Muhammad Faizan Akram (FA23-BBD-090)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#

# Class of Account:
class Account:

#---------------------------------------------------------------------------------------------#
    # Constructor (Initialization Method)
    def __init__(self, account_id, account_name, account_type, balance):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__account_type = account_type
        self.__balance = balance

#---------------------------------------------------------------------------------------------#
    # Accessor methods
    def get_account_id(self):
        return self.__account_id

    def get_account_name(self):
        return self.__account_name

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

#---------------------------------------------------------------------------------------------#
    # Mutator methods
    def set_account_name(self, account_name):
        self.__account_name = account_name

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance

#---------------------------------------------------------------------------------------------#
    # Other methods
    def add_account(self):
        pass

    def update_account(self):
        pass

    def check_balance(self):
        return self.__balance
    
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#

# Class of Transaction:
class Transaction:

#---------------------------------------------------------------------------------------------#
    # Constructor (Initialization Method)
    def __init__(self, transaction_id, date, amount, transaction_type, account):
        self.__transaction_id = transaction_id
        self.__date = date
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__account = account

#---------------------------------------------------------------------------------------------#
    # Accessor methods
    def get_transaction_id(self):
        return self.__transaction_id

    def get_date(self):
        return self.__date

    def get_amount(self):
        return self.__amount

    def get_transaction_type(self):
        return self.__transaction_type

    def get_account(self):
        return self.__account

#---------------------------------------------------------------------------------------------#
    # Mutator methods
    def set_date(self, date):
        self.__date = date

    def set_amount(self, amount):
        self.__amount = amount

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def set_account(self, account):
        self.__account = account

#---------------------------------------------------------------------------------------------#
    # Other methods
    def record_transaction(self):
        pass

    def update_account_balance(self):
        pass
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#