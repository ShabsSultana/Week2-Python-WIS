#asks user user for integer and count down to 1, displaying number each time

def countdown():
    print("Welcome to countdown")
    #asks user to pic number and cast to number as an integer
    number = int(input("Pick a number: "))

    #while number is larger than zero, loop will print the number and take away 1 from number and assign value to number
    while (number > 0):
        print(number)
        number = number - 1
#end of function

#calls coundown function
countdown()