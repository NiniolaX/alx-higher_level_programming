#!/usr/bin/python3

while True:
    print("Enter your age:")
    age = input()

    try:
        age = int(age)
    except Exception:
        print("Please use numeric digits.")
        continue
    if age < 1:
        print("Please enter a positive number.")
        continue # Not necessary, just for readability
    else:
        print(f"Your age is {age}.")
        break