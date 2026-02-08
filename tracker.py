import os
import json
import random
import string
import time

expenses = []
deleted_expenses = []

def load_expenses():
    global expenses
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    else:
        expenses = []

def load_deleted_expenses():
    global deleted_expenses
    if os.path.exists('deleted_expenses.json'):
        with open('deleted_expenses.json', 'r') as f:
            deleted_expenses = json.load(f)
    else:
        deleted_expenses = []

def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=3)

def save_deleted_expenses():
    with open('deleted_expenses.json', 'w') as f:
        json.dump(deleted_expenses, f, indent=3)

# Helper for add_expense and update_expenses
def add_fields(prompt, err_msg, max_len):
    while True:
        expense = input(prompt)
        if expense and len(expense) < max_len:
            return expense
        print(err_msg)

# Helper for add_expense and update_expesne
def check_if_int(prompt):
    while True:
        try:
            amount = int(input(prompt))
            if amount and amount >= 1:
                return amount
        except:
            invalid_input_message()

def if_input_0_break(input):
    if input == '0':
        process_stopped_message()
        return False
    return True

def check_expenses_exists(expenses):
    if not expenses:
        no_expense_message()
        return False
    return True

def all_function_header(text):
    print('\n')
    for char in text:
        print(char.upper(), end='', flush=True)
        time.sleep(0.02)
    time.sleep(0.5)

# Messages
def success_message():
    print('\n✅ Process was successfull!')

def fail_message():
    print('\n❌ Process was not successfull!')

def no_expense_message():
    print('\n❌ No expense added yet!')

def id_not_exist_message():
    print('\n❌ Expense ID does not exists!')

def invalid_input_message():
    print('\n❌ Invalid input! Please enter a valid input')

def process_successfull_message():
    print('\n✅ Process was successfull!')

def process_stopped_message():
    print('\n⛔ Process was stopped!')

def no_result_found_message(category):
    print(f'\n❌ No result found for {category.lower()}')

load_expenses()
load_deleted_expenses()

def add_expense():
    all_function_header('|| ---> Adding an expense <--- ||\n')
    while True: 
            title = add_fields('\nEnter expense title: ', '\n❌ Len of title must be (1-16)!', 16)
            amount = check_if_int('\nEnter expense amount: ')
            category = add_fields('\nEnter expense category: ', '\n❌ Len of category must be (1-16)!', 16)
            note = add_fields('\nEnter a short expense note: ', '\n❌ Len of note must be (1-36)!', 36)
            id = ''.join(random.sample(string.digits, 4))

            data = {
                'title': title.title(),
                'amount': amount,
                'category': category.lower(),
                'note': note.capitalize()
            }

            expenses.append({id:data})
            save_expenses()
            success_message()
            return

def delete_expense():
    if not check_expenses_exists(expenses):
        return
    
    all_function_header('|| ---> Deleting an expense <--- ||\n')

    while True:
        expense_id = input('\nEnter expense ID: ')

        if not if_input_0_break(expense_id):
            return

        for expense in expenses:
            for key in expense.keys():
                if expense_id == key:
                    expenses.remove(expense)
                    deleted_expenses.append(expense)
                    save_expenses()
                    save_deleted_expenses()
                    success_message()
                    return
        id_not_exist_message()

def update_expense():
    if not check_expenses_exists(expenses):
        return
    
    all_function_header('|| ---> Updating an expense <--- ||\n')

    expense_id = input('\nEnter expense ID: ')

    if not if_input_0_break(expense_id):
        return

    for expense in expenses:
        for key in expense.keys():
            if expense_id == key:
                all_fields = ['title', 'amount', 'category', 'note']

                while True:
                    field = input('\nEnter [title], [amount], [category], [note]: ').lower()

                    if field in all_fields:
                        if field == all_fields[0]:
                            updated_field = add_fields('\nEnter new expense title: ', '\n❌ Len of title must be (1-16)!', 16)
                            expense[key][field] = updated_field.title()

                        elif field == all_fields[1]:
                            updated_field = check_if_int('\nEnter new expense amount: ')

                        elif field == all_fields[2]:
                            updated_field = add_fields('\nEnter new expense category: ', '\n❌ Len of category must be (1-16)!', 16)
                            expense[key][field] = updated_field.lower()

                        elif field == all_fields[3]:
                            updated_field = add_fields('\nEnter new expense note: ', '\n❌ Len of note must be (1-36)!', 36)
                            expense[key][field] = updated_field.capitalize()

                        save_expenses()
                        success_message()
                        return
                    else:
                        invalid_input_message()
    id_not_exist_message()
    
def delete_all_expenses():
    if not check_expenses_exists(expenses):
        return
    
    all_function_header('|| ---> Deleting all expenses <--- ||\n')

    match input('\nAre you sure you want to delte all expenses (y/n): ').lower():
        case 'n':
            process_stopped_message()
        case 'y':
            expenses.clear()
            save_expenses()
            success_message()
            print()
        case _ :
            print('\nPlease enter (y/n)!')

def filter_by_category():
    if not check_expenses_exists(expenses):
        return
    
    all_function_header('|| ---> Filtering expenses <--- ||\n')

    category = input('\nEnter category: ').lower()
    filtered_expense = [list(expense.values())[0]
                        for expense in expenses
                        if list(expense.values())[0]['category'] == category]
    
    if not filtered_expense:
        no_result_found_message(category)
        return
        
    headers = f'{'TITLE':<18} {'AMOUNT':<8} {'CATEGORY':<18} {'NOTE'}'

    print('-'*90)
    print(headers)
    print('-'*90)
    for expense in filtered_expense:
        print(f'{expense['title']:<18} ${expense['amount']:<8} {expense['category']:<18} {expense['note']}')

# Use to calculate total for all expenses and deleted expenese
def total_expense(lst):
    total = []
    for expense in lst:
        for key in expense.keys():
            amount = expense[key]['amount']
            total.append(amount)
    return total

def view_all_expenses():
    if not check_expenses_exists(expenses):
        return
    
    all_function_header('|| ---> Viewing all expenses <--- ||\n')
    
    headers = f'{'ID':<6} {'TITLE':<18} {'AMOUNT':<8} {'CATEGORY':<18} {'NOTE'}'

    print('-'*90)
    print(headers)
    print('-'*90)
    for expense in expenses:
        for key in expense.keys():
            print(f'{key:<6} {expense[key]['title']:<18} ${expense[key]['amount']:<8} {expense[key]['category']:<18} {expense[key]['note']}')

    total = total_expense(expenses)
    print('-'*30)
    print(f'Total Expense: ${sum(total):.2f}')

def view_deleted_expenses():
    if not check_expenses_exists(deleted_expenses):
        return
    
    all_function_header('|| ---> Viewing deleted expenses <--- ||\n')

    headers = f'{'ID':<6} {'TITLE':<18} {'AMOUNT':<8} {'CATEGORY':<18} {'NOTE'}'

    print('-'*90)
    print(headers)
    print('-'*90)
    for expense in deleted_expenses:
        for key in expense.keys():
            print(f'{key:<6} {expense[key]['title']:<18} ${expense[key]['amount']:<8} {expense[key]['category']:<18} {expense[key]['note']}')

    total = total_expense(deleted_expenses)
    print('-'*30)
    print(f'Total Expense: ${sum(total):.2f}')

def intro():
    print('\n')
    text = '|--|--| ** --> EXPENSE TRACKER <-- ** |--|--|'
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.03)
    time.sleep(1)

def ending():
    print('\n')
    text = '|| ** --> ❤️ BYE! HOPE YOU LIKED IT ❤️ <-- ** ||'
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.03)
    time.sleep(1)

def instruction_manual():
    current_dir = os.getcwd()
    print(f'''
          
EXPENSE TRACKER GUIDE:

1. ADD EXPENSE           - Add expense by adding different fields.
2. UPDATE EXPENSE        - Update anything you want.
3. DELETE EXPENSE        - Delete expenses by ID.
4. FILTER BY CATEGORY    - Filter your tasks by category
5. VIEW ALL EXPENSES     - See current expenses with total expense
6. VIEW DELETED EXPENSES - See deleted expenses with total expense
7. DELETE ALL EXPENSES   - Reset everything
8. EXIT EXPENSE TRACKER  - Program will exit

- Enter '0' to stop deleting or updating
- Every expense will be saved at {os.path.join(current_dir, 'expenses.json')}
- Every deleted expense be be saved at {os.path.join(current_dir, 'deleted_expenses.json')}
- If all expenses are deleted at on they will be gone forever.
''')

def main():
    intro()
    instruction_manual()

    all_funcs = [add_expense, update_expense, delete_expense, filter_by_category,
                  view_all_expenses, view_deleted_expenses, delete_all_expenses]

    while True:
        try:
            user_choice = int(input('\nEnter (1-8): '))

            if user_choice == 8:
                ending()
                break

            all_funcs[user_choice - 1]()

        except IndexError:
            invalid_input_message()
        except ValueError:
            invalid_input_message()
