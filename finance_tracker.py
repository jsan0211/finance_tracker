import datetime
import random
import string
import csv
import os

# def set_save_location():

def write_log(log_name, log_entry):
    file_exists = os.path.exists(log_name)
    write_header = not file_exists or os.path.getsize(log_name) == 0

    with open(log_name, "a", newline="") as file:
        fieldnames = ["Purchase ID", "Date/Time", "Category", "Amount", "Location"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow(log_entry)


#def write_log(log_name, log_entry):
#   with open(log_name, "a", newline="") as file:
#        writer = csv.writer(file)
#        writer.writerow([
#            log_entry["Purchase ID"],
#            log_entry["Date/Time"],
#            log_entry["Category"],
#            log_entry["Amount"],
#            log_entry["Location"]
#        ])


def generate_random_key():
    characters = string.ascii_letters + string.digits + string.punctuation
    purchase_id = ''.join(random.choices(characters, k=16))
    return purchase_id

def create_categories():
    categories_list = []
    if len(categories_list) == 0:
        choice = input("You have not set your categories do you want to create one or use default? Enter C or D: ")
        choice.lower()
        if choice == "c":
            enter_categories = input("Enter your categories seperated by commas: ")
            enter_categories = enter_categories.split(",")
            for word in enter_categories:
                word = word.strip().lower()
                categories_list.append(word)
            return categories_list
        elif choice == "d":
            categories_list = [
                "Rent/Mortgage",
                "Utilities (Electricity, Gas, Water)",
                "Groceries",
                "Dining Out",
                "Transportation (Gas, Public Transit, Parking)",
                "Entertainment (Movies, concerts, etc.)",
                "Healthcare (Doctor visits, medications)",
                "Insurance (Health, car, renters/homeowners)",
                "Taxes",
                "Clothing",
                "Personal Care (Haircuts, toiletries)",
                "Education (Tuition, books, online courses)",
                "Travel",
                "Gifts",
                "Donations",
                "Debt Payments (Credit cards, loans)",
                "Savings",
                "Investments",
                "Income (Salary, freelance, etc.)",
                "Other"
            ]
            return categories_list
        else:
            print("Please select a valid option. Enter C for create or D for default categories.")
    else:
        return categories_list # should have probably been a while loop to have the user go back and make valid selection
    
def select_category(categories_list):
    for index, category in enumerate(categories_list):
        print(f"{index}. {category}")
    selected_index = int(input("select a category from the list by number. Example: 1 "))
    return categories_list[selected_index]

def log_purchases(purchase_id, category):
    location = input("Where was the purchase made?: ")
    amount = input("How much was the purchase?: ")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # instead of datetime.datetime.now()
    amount = round(float(amount), 2)  # ensure currency looks like "45.00"


    # return a dictionary to use in write_log()
    log = {
        "Purchase ID": purchase_id,
        "Date/Time": date_time,
        "Category": category,
        "Amount": amount,
        "Location": location,
    }
    return log

def main():
    categories = create_categories()
    category = select_category(categories)

    while True:
        purchase_id = generate_random_key()
        log_entry = log_purchases(purchase_id, category)
        write_log("expenses.csv", log_entry)

        # Ask if user wants to log another purchase
        while True:
            keep_logging_choice = input("Log another purchase? (y/n): ").lower()
            if keep_logging_choice in ("y", "n"):
                break
            print("Invalid option. Please enter y/n.")

        if keep_logging_choice == "n":
            break

        # Ask if user wants to use the same category
        while True:
            same_category = input("Use same category? (y/n): ").lower()
            if same_category == "n":
                category = select_category(categories)
                break
            elif same_category == "y":
                break
            else:
                print("Invalid option. Please enter y/n.")

print(main())
