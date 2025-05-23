# DatabaseRead handles reading and filtering transactions and categories from CSV files
class DatabaseRead():
    def __init__(self, trans_file_name, cat_file_name):
        # Initialize with file names and empty lists
        self.categories = CategoryList()
        self.transactions = TranscationList()
        self.trans_file_name = trans_file_name
        self.cat_file_name = cat_file_name

    def get_categories(self):
        # Read categories from CSV and store in CategoryList
        categories = []
        try:
            with open(self.cat_file_name, "r") as file:
                data = file.readlines()
                for line in data[1:]:
                    category = line.split(",")
                    categories.append({
                        "name": category[0],
                        "type": category[1][:-1]
                    })
            self.categories.set_categories(categories)
        except FileNotFoundError:
            print(f"Error: File {self.cat_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while reading categories: {e}")
        
    def get_transactions(self):
        # Read transactions from CSV and store in TranscationList
        transactions = []
        self.get_categories()
        try:
            with open(self.trans_file_name, "r") as file:
                data = file.readlines()
                for line in data[1:]:
                    transaction = line.split(",")
                    transactions.append({
                        "date": transaction[0],
                        "amount": transaction[1],
                        "destination": transaction[2][:-1],
                        # Lookup category type by destination name
                        "category": self.categories.get_category_by_name(transaction[2][:-1])[0]["type"]
                    })
            self.transactions.set_transactions(transactions)
        except FileNotFoundError:
            print(f"Error: File {self.trans_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while reading transactions: {e}")

    def all_transactions(self):
        # Print all transactions in a formatted way
        all = ""
        for x in self.transactions.get_transactions():
            all += x["date"] + " : " + x["amount"] + " : " + x["destination"] + " : " + x["category"] + "\n"
        print("Date, Ammount, Destination, Category")
        print(all)

    def get_transactions_by_cat(self, cat):
        # Print transactions filtered by category
        sortcat = ""
        for x in self.transactions.get_transactions():
            if x["category"] == cat:
                sortcat += x["date"] + " : " + x["amount"] + " : " + x["destination"] + "\n"
        print("Date, Ammount, Destination")
        print(sortcat)

    def date_transactions(self, date):
        # Print transactions filtered by date
        self.transactions.print_transactions_by_date(date)
    
    def destination_transtations(self,destination):
        # Print transactions filtered by destination
        self.transactions.print_transactions_by_destination(destination)

####################################################

# CategoryList manages a list of categories and provides lookup methods
class CategoryList():
    def __init__(self):
        self.categories = []

    def get_category_by_type(self, typee):
        # Return all categories with a given type
        categories_list = []
        for cat in self.categories:
            if cat["type"] == typee:
                categories_list.append({
                    "name": cat["name"],
                })
        return categories_list

    def get_category_by_name(self, name):
        # Return the type for a given category name
        categories_list = []
        for cat in self.categories:
            if cat["name"] == name:
                categories_list.append({
                    "type": cat["type"],
                })
        return categories_list

    def get_categories(self):
        return self.categories

    def set_categories(self, cat_list):
        self.categories = cat_list

#################################################

# TranscationList manages a list of transactions and provides filtering/printing
class TranscationList():
    def __init__(self):
        self.transactions = []

    def set_transactions(self, trans_list):
        self.transactions = trans_list

    def get_transactions(self):
        return self.transactions

    def get_transactions_by_destination(self, destination):
        # Return transactions for a specific destination
        transactions_list = []
        for trans in self.transactions:
            if trans["destination"] == destination:
                transactions_list.append({
                    "date": trans["date"],
                    "amount": trans["amount"]
                })
        return transactions_list

    def get_transactions_by_date(self, date):
        # Return transactions for a specific date
        transactions_list = []
        for trans in self.transactions:
            if trans["date"] == date:
                transactions_list.append({
                    "destination": trans["destination"],
                    "amount": trans["amount"],
                    "category": trans["category"]
                })
        return transactions_list

    def print_transactions_by_destination(self, destination):
        # Print transactions for a specific destination
        printed_trans = "Date" + (" " * 7) + "| Ammount\n"
        printed_trans += ("~" * 20) + "\n"
        trans_list = self.get_transactions_by_destination(destination)
        for exp in trans_list:
            printed_trans += exp["date"] + " | " + exp["amount"] + "\n"
        print(printed_trans)

    def print_transactions_by_date(self, date):
        # Print transactions for a specific date
        printed_trans = "Destination | Ammount\n"
        printed_trans += ("~" * 18) + "\n"
        trans_list = self.get_transactions_by_date(date)
        for exp in trans_list:
            printed_trans += exp["destination"] + " | " + exp["amount"] + "\n"
        print(printed_trans)

#######################################

# DatabaseWrite handles appending new transactions to the CSV file
class DatabaseWrite():
    def __init__(self, trans_file_name, date, amount, destination):
        self.input_data = []
        self.trans_file_name = trans_file_name
        self.date = date
        self.amount = amount
        self.destination = destination

    def add_data(self):
        # Append a new transaction to the CSV file
        self.input_data = [self.date, "," , self.amount, "," , self.destination]
        with open(self.trans_file_name, 'a') as file:
            file.writelines(self.input_data)
            file.writelines("\n")

#################################

# --- Main program starts here ---
cat_file_name = "Categories.csv"
name = str(input("Welcome to Where Is My Money, please enter your name to start: "))
trans_file_name = input("Welcome %s, please enter your transactions file name :" %name)+".csv"
trans_file_name = "Transactions.csv"
print("Now we are ready to begin!")
print("Please select what you would like to do:")
print("Option A: View Transactions")
print("Option B: Add a transaction")

database = DatabaseRead(trans_file_name, cat_file_name)
database.get_transactions()
accepted_options = ["A","B"]
accepted_options2 = ["1", "2", "3", "4"]

while True:
    option = str(input("Please select the letter of the option you want: ")).capitalize()
    if option not in accepted_options:
        print("Please select from Options A, B or C only")
        continue
    else:
        break

if option == "A":
    # Transaction viewing options
    print("Please select the transaction viewing type")
    print("Option 1: View all transactions")
    print("Option 2: Filter transactions by category")
    print("Option 3: Filter transactions by date")
    print("Option 4: Filter transactions by destination")
    while True:
        option2 = str(input("Please select the number of the option you want: ")).capitalize()
        if option2 not in accepted_options2:
            print("Please select from Options 1, 2, 3 or 4 only")
            continue
        else:
            break
    if option2 == "1":
        database.get_transactions()
        database.all_transactions()

    elif option2 == "2":
        print("Categories are: Housing, Transportation, Food")
        cat_of_choice = input("Please enter the category you wish to filter with: ").capitalize()
        database.get_transactions()
        database.get_transactions_by_cat(cat_of_choice)

    elif option2 == "3":
        date_of_choice = input("Please enter the date you wish to filter with: ").capitalize()
        database.get_transactions()
        database.date_transactions(date_of_choice)

    elif option2 == "4":
        destination_of_choice = input("Please enter the destination you wish to filter with: ").capitalize()
        database.get_transactions()
        database.destination_transtations(destination_of_choice)

elif option == "B":
    # Add a new transaction
    def add_transaction():
        date = input("Please enter the date of the transcation here: ")
        amount = input("Please enter the amount of the transaction here: ")
        destination = input("Please the destination of the transactions here: ")
        dataWrite = DatabaseWrite(trans_file_name, date, amount, destination)
        dataWrite.add_data()
        database.get_transactions()
    add_transaction()
    print("Here is the full transactions after adding the transaction")
    database.all_transactions()