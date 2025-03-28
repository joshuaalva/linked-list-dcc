

print("Boudreaux's Barbershop")
# write to logic for the CLI program 
# Select an the number for the action you wish to perform and then hit enter
# prompt the user to choose from a menu of actions to take 
print("1. Add a new client")
print("2. Display a list of all current clients")
print("3. Search for a client")
print("4. Delete a client")
print("5. Quit")
print("What do you want to do?")

answer = int(input("Type the number for the action you wish to perform and hit Enter."))
while answer < 1 or answer > 5:
    answer = int(input("Try again. That is not a given option"))
if answer == 1: 
        print("Add a new client")
        fName = input("Provide the client's first name: ")
        pNumber = input("Provide the clients phone number: ")
        dateOfBirth = input("Provide the cleints D.O.B in MMDDYYYY: ")
        newCustomer = print(f"{fName}, {pNumber}, {dateOfBirth}")
if answer == 2:
        print("Display a list of all current clients")
if answer == 3: 
        print("Search for a client")
if answer == 4: 
        print("Delete a client")
if answer == 5:
        print("Quit")

