def add(a, b): 
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "/n")

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "/n")

def multiply(a, b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer) + "/n")

def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "/n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        subtract(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        multiply(a, b)
    elif choice == "d" or choice == "D":
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        divide(a, b)
    elif choice == "e" or choice == "E":
        print("Program Ended")
        quit()
    else:
        print("Invalid choice")
