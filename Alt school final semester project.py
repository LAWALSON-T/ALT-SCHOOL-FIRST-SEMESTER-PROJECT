import uuid

from datetime import datetime , timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        
    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
            
        self.updated_at = datetime.utcnow()
    
            
    def to_dict(self):
        expense_dict = {
            "id" : self.id,
            "title" : self.title,
            "amount" : self.amount,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at
        }
        return expense_dict 
        
    
class ExpenseDatabase:
        def __init__(self):
            self.expenses = []

        def add_expense(self, expense):
            self.expenses.append(expense)

        def remove_expense(self, expense_id):
            exist= False
            for i in self.expenses:
                if i.id == expense_id:
                    self.expenses.remove(i)
                    exist = True
            if exist == False:
                print(f'expenses with expense id {expense_id} does not exist')

        def get_expense_by_id(self, expense_id):
            for i in self.expenses:
                if i.id==expense_id:
                    return i

        def get_expense_by_title(self, expense_title):        
            expense_list = [i for i in self.expenses if i.title == expense_title]   
            return expense_list  

        
        def to_dict(self):
            dict_list= [i.to_dict() for i in self.expenses ]
            return dict_list
        
    
    
    