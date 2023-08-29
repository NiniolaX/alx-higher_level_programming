print("Program Start: success")

a = 5

try:
    b = int(input("Enter a number: "))
    print("Result: ", a/b)
except ValueError:
    print("That was not a valid number. Try again..")
except ZeroDivisionError as z:
    print("Cannot divide by zero. Try again..")
except Exception as e:
    print("Error:", e)

print("Program End: success")
