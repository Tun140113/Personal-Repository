import os
import sys
import shutil
from datetime import datetime
import time
width = shutil.get_terminal_size().columns
os.system("cls")
print(("Time: " + datetime.now().strftime("%H:%M:%S")).center(width))
def check_password():
    print("PLEASE ENTER YOUR PASSWORD".center(width))
    password = input(">>>")
    length = len(password)
    score = 0 
    if length >= 8:
        score += 1
    
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
        
    if has_lower:
        score += 1
    
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper:
        score += 1

    has_digit = False
    for char in password: 
        if char.isdigit():
            has_digit = True
            break
    if has_digit: 
        score += 1

    has_symbol = False
    for char in password:
        if not char.isalnum() and not char.isspace():
            has_symbol = True
            break
    if has_symbol:
        score += 1       
    os.system("cls")
    print(f"Your password is {password}")
    print(f"Your password length is: {length}")
    print(f"Your score is: {score}/5".center(width))
    time.sleep(1)
    print ("------------------".center(width))
    if score <= 2:
        print("❌ Weak password".center(width))
    elif score <= 4:
        print("⚠ Medium password".center(width))
    else:
        print("✅ Strong password".center(width))
        time.sleep(0.5)
        print("---Programme finished---".center(width))
check_password()

