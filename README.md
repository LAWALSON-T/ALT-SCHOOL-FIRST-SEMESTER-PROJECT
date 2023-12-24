# ALT-SCHOOL-FIRST-SEMESTER-PROJECT
OOP PROJECT The goal of this assignment is to assess understanding of object-oriented programming (OOP) concepts in Python
# Project Description
The project requires creating two classes expense class and expense database class. The expense class uses the uuid library to track and provide accurate time for each transaction, update and entry. The expense class contains three methods, the init method which Initializes the attributes, the update method and the to_dict method. The update method updates the original attributes such as the title and/or amount, as well as updating of the time it takes for the action to be intitiated, while the to_dict method converts all entry to dictionary for record keeping. 
The expense database class acts as a database with it being able to carry out database functions CRUD, Create, read, update and delete. all these functions are present in the methods which are the init method which Initializes the list, the add_expense method adds an expense to the class database, the remove_expense method which removes an expense, the get_expense_by_id method retrieves an expense by ID, the get_expense_by_title method retrieves expenses by title, the to_dict method returns a list of dictionaries representing expenses.
Using the expense class you can add entries to the database class, and then manipulate the entries wsing the methods in the expense class and expense database class
# How to clone the repo
Open Terminal or Command Prompt
-Open a terminal window or command prompt on your local machine
Navigate to the Directory Where You Want to Clone the Repository:
-Use the cd command to move to the directory where you want to place the cloned repository
-cd path/to/your/desired/directory
Clone the Repository:
-Use the git clone command followed by the repository URL obtained earlier. For HTTPS:
-git clone https://github.com/username/repository.git
# How to use the class
## Creating Expenses:
initiate the expense database class and put it in a variable
market= ExpenseDatabase()

### you can add to the expense class and update it
Instantiate an Expense object by providing a title and an amount. For example
market_yam = Expense("two tubers of yam", 23.45)
market_yam.update("three tubers of yam ", 35.7)
### or just add entries to the class
market_rice = Expense("one bag of rice", 100.56)
### Using the instance of the expense database class you can call the varying methods
market.add_expense(market_rice)
market.add_expense(market_yam)
### to convert entries to a dictionary
market.to_dict()
### to use the get_expense_by_id method
search_expense=market.get_expense_by_id('3247c5e4-457b-4a54-b55b-4d0a08370b2b')
search_expense.title
### to remove and entry from the record
market.remove_expense('a229e386-4a98be1a8527daeb')
### to get an entry using the title
d=market.get_expense_by_title('modul of garri')
d=d[0]
d.amount

so these are the ways to use the class 
