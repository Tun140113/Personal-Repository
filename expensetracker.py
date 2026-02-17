import os
import shutil
import time
import sys
from datetime import datetime

width = shutil.get_terminal_size().columns
os.system("cls")


def add_expense():

    # CATEGORY
    while True:
        print("Please enter the expense category".center(width))
        category = input("My expense category is: ")

        if " " in category:
            print("Category cannot contain spaces!".center(width))
            time.sleep(1)
            os.system("cls")
        else:
            break

    # NAME
    while True:
        print("Please enter the expense name".center(width))
        name = input("My expense name is: ")

        if " " in name:
            print("Name cannot contain spaces!".center(width))
            time.sleep(1)
            os.system("cls")
        else:
            break

    # AMOUNT
    while True:
        print("Please enter the expense amount".center(width))
        amount = input("The amount of this expense is: ")

        try:
            amount = int(amount)
            break
        except ValueError:
            print("The amount must be a number!")
            time.sleep(1)
            os.system("cls")

    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{category}|{name}|{amount}\n")

    print("Expense added successfully!")
    time.sleep(1)
    os.system("cls")



def view_expenses():
    print("Press Enter to view all expenses")
    input()

    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                category, name, amount = parts

                os.system("cls")
                print("Category:", category,
                      "| Expense:", name,
                      "| Amount:", amount, "VND")
                input()
                os.system("cls")

    except FileNotFoundError:
        os.system("cls")
        print("Cannot locate file. Have you added any expenses yet?".center(width))
        input()


def statistics():
    total_money = 0
    stats = {}

    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                category, name, amount = parts
                amount = int(amount)

                total_money += amount
                stats[category] = stats.get(category, 0) + amount

        print("Total money spent:", total_money, "VND")
        print("\nStatistics by category:")

        for category, total in stats.items():
            print(category, ":", total)

        max_category = None
        max_amount = 0

        for category, total in stats.items():
            if total > max_amount:
                max_amount = total
                max_category = category

        print("\nHighest spending category:", max_category, "-", max_amount, "VND")
        input()

    except FileNotFoundError:
        print("No data found.")
    except ValueError:
        print("Data format error.")


while True:
    print("_____________________".center(width))
    print(("Time: " + datetime.now().strftime("%H:%M:%S")).center(width))
    print("Welcome to the Family Expense Tracking System!".center(width))
    print("(1) Add expense")
    print("(2) View expenses")
    print("(3) Show statistics")
    print("(4) Exit")

    choice = input("My choice: ")

    if choice == "1":
        os.system("cls")
        print("Loading...".center(width))
        time.sleep(1)
        os.system("cls")
        add_expense()

    elif choice == "2":
        os.system("cls")
        print("Loading...".center(width))
        time.sleep(1)
        os.system("cls")
        view_expenses()

    elif choice == "3":
        os.system("cls")
        print("Loading...".center(width))
        time.sleep(1)
        os.system("cls")
        statistics()

    elif choice == "4":
        os.system("cls")
        print("Goodbye! See you next time.".center(width))
        input()
        sys.exit()
