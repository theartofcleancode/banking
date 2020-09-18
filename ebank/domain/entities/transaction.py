from datetime import datetime as date

class Transaction:
    def __init__(self, action, amount, client_name, account_code, old_balance, new_balance):
        self.action = action
        self.amount = amount
        self.client_name = client_name
        self.account_code = account_code
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.time = date.now().ctime()

    def to_dict(self):
        d = self.__dict__
        del d['time']
        return d