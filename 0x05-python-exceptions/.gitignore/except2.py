# Opens a file

print("START")
print("Enter file name: ")
filename = input()

try:
    myfile = open(filename, 'r')
except FileNotFoundError:
    print("Error: File does not exist")
else:
    try:
        print(myfile.read())
    finally:
        myfile.close()

finally:
    print("END")
