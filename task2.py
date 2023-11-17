import json



# Initialize an empty budget

budget = {

    "income": 0,

    "expenses": []

}



def record_income(amount):

    budget["income"] += amount

    save_budget()



def record_expense(category, amount):

    expense = {

        "category": category,

        "amount": amount

    }

    budget["expenses"].append(expense)

    save_budget()



def calculate_budget():

    income = budget["income"]

    total_expenses = sum(expense["amount"] for expense in budget["expenses"])

    return income - total_expenses



def categorize_expenses():

    categories = {}

    for expense in budget["expenses"]:

        category = expense["category"]

        amount = expense["amount"]

        if category not in categories:

            categories[category] = amount

        else:

            categories[category] += amount

    return categories



def save_budget():

    with open('budget.json', 'w') as file:

        json.dump(budget, file)



def load_budget():

    try:

        with open('budget.json', 'r') as file:

            global budget

            budget = json.load(file)

    except FileNotFoundError:

        budget = {

            "income": 0,

import json



# Initialize an empty budget

budget = {

    "income": 0,

    "expenses": []

}



def record_income(amount):

    budget["income"] += amount

    save_budget()



def record_expense(category, amount):

    expense = {

        "category": category,

        "amount": amount

    }

    budget["expenses"].append(expense)

    save_budget()



def calculate_budget():

    income = budget["income"]

    total_expenses = sum(expense["amount"] for expense in budget["expenses"])

    return income - total_expenses



def categorize_expenses():

    categories = {}

    for expense in budget["expenses"]:

        category = expense["category"]

        amount = expense["amount"]

        if category not in categories:

            categories[category] = amount

        else:

            categories[category] += amount

    return categories



def save_budget():

    with open('budget.json', 'w') as file:

        json.dump(budget, file)



def load_budget():

    try:

        with open('budget.json', 'r') as file:

            global budget

            budget = json.load(file)

    except FileNotFoundError:

        budget = {

            "income": 0,

            "expenses": []

        }



# Load existing budget from the file (if any)

load_budget()



while True:

    print("\nBudget Tracker Menu:")

    print("1. Record Income")

    print("2. Record Expense")

    print("3. Calculate Budget")

    print("4. Analyze Expenses")

    print("5. Exit")

    choice = input("Enter your choice: ")



    if choice == "1":

        amount = float(input("Enter income amount: "))

        record_income(amount)

        print(f"Income recorded: {amount}")



    elif choice == "2":

        category = input("Enter expense category: ")

        amount = float(input("Enter expense amount: "))

        record_expense(category, amount)

        print(f"Expense recorded: {category} - {amount}")



    elif choice == "3":

        remaining_budget = calculate_budget()

        print(f"Remaining Budget: {remaining_budget}")



    elif choice == "4":

        expenses_by_category = categorize_expenses()

        print("Expenses by category:")

        for category, amount in expenses_by_category.items():

            print(f"{category}: {amount}")



    elif choice == "5":

        save_budget()

        print("Exiting the Budget Tracker application. Your transactions are saved.")

        break￼Enter            "expenses": []

        }



# Load existing budget from the file (if any)

load_budget()



while True:

    print("\nBudget Tracker Menu:")

    print("1. Record Income")

    print("2. Record Expense")

    print("3. Calculate Budget")

    print("4. Analyze Expenses")

    print("5. Exit")

oice = input("Enter your choice: ")



    if choice == "1":

        amount = float(input("Enter income amount: "))

        record_income(amount)

        print(f"Income recorded: {amount}")



    elif choice == "2":

        category = input("Enter expense category: ")

        amount = float(input("Enter expense amount: "))

        record_expense(category, amount)

        print(f"Expense recorded: {category} - {amount}")



