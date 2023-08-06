def main():

    print("This program converts US dollars to Pounds Sterling and euro")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars) 
    euro = convert_to_euro(dollars)
    pesos = convert_to_pesos(dollars)
    
    while True:
        conversion_choice = input("Convert to pounds, pesos,euro or exit the program ").lower()

        if conversion_choice == "pounds":
            print("That is", pounds, "pounds. ")
        elif conversion_choice == "euro":
            print("That is ", euro, "in euro. ")
        elif conversion_choice == "pesos":
            print("This is", pesos, "in pesos.") 
        elif conversion_choice == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid conversion choice. Please choose either 'pounds', 'pesos', 'euro'or 'exit'.")
            conversion_choice
def convert_to_pounds(dollars):
    return dollars * 0.78

def convert_to_euro(dollars):
    return dollars * 0.90

def convert_to_pesos(dollars):
    return dollars * 17.08
main()

