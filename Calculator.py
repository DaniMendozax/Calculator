menu = """
        Welcome to you calculator App 🧮
            1 - Add
            2 - Rest
            3 - Multiplication
            4 - Division
        Please enter a valid option: """
 
flag_option = True
 
 
def operation(value):
    flag_entries = True
    while flag_entries:
        try:
            n1 = int(input("Entry a first number: "))
            n2 = int(input('Entry a second number: '))
            flag_entries = False
 
        except:
            print("\nPlease, entry a valid value\n")
 
    if value == '1':
        return n1 + n2
    elif value == '2':
        return n1 - n2
    elif value == '3':
        return n1 * n2
    elif value == '4':
        return n1 / n2
 
while flag_option:
    option = input(menu)

    if option == '1' or option == '2' or option == '3' or option == '4':
        print("The answer is " + str(operation(option)))
        flag_option = False
    else:
        print("Please enter a valid option")



    