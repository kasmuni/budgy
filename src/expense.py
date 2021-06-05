# Expense Class
import itertools

class Expense:
    id_iter = itertools.count()

    def __init__(self, name, category):
        self.id = next(Expense.id_iter)
        self.name = name
        self.category = category
        self.balance = 0

    def expense_event(self, amount):
        self.balance += amount

    def get_expense_balance(self):
        return self.balance

    def get_expense_name(self):
        return self.name

    def get_expense_category(self):
        return self.category
