#Asks user to assign a and b to be true or false, then prints a AND b

def get_user_boolean_input():
    user_input = "Hello"

    #if the input is not true AND is not false, keep asking to enter true or false
    while ((user_input != "True") and (user_input != "False")):
        user_input = input("Enter True or False ")
    
    #if the input is true or false, assign to user_input_boolean
    if (user_input == "True"):
        user_input_boolean = True
    
    else:
        user_input_boolean = False

    #returns user_input_boolen variable
    return (user_input_boolean)

    #end of function

a = get_user_boolean_input()
b = get_user_boolean_input()

print(str(a) + " AND " + str(b) + " is: ")
print(a and b)


    