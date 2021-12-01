print("What is your operation: add, subtract, multiply, divide")
question = input() #input

#functions
def add(int1, int2):
    sum = int1 + int2
    print("the sum is " + str(sum))

def subtract(int1, int2):
    difference = int1 - int2
    print("the difference is " + str(difference))

def multiply(int1, int2):
    product = int1 * int2
    print("the product is " + str(product))

def divide(int1, int2):
    quotient = int1/int2
    print("the quotient is " + str(quotient))


#for Adding one_num and two_num
if question == "add": #if statement
    print("what is your first number")
    one_num = int(input())
    while one_num >= 200: #while loop
        print("the number is too high. what is your first number")
        one_num = int(input())

    print("what is your second number")
    sec_num = int(input())

    while sec_num >= 200:
        print("the number is too high. what is your second number")
        sec_num = int(input())

    add(one_num, sec_num)

#for Subtracting third_num and fourth_num
if question == "subtract":
    print("what is your first number?")
    third_num = int(input())
    while third_num <= 10:
        print("it's 2 low. what is your first number?")
        third_num = int(input())

    print("what is your second number?")
    fourth_num = int(input())
    while fourth_num <= 10:
        print("it is too low. what is your second number?")
        fourth_num = int(input())

    subtract(third_num, fourth_num)

#for multiplication fifth_num and sixth_num
if question == "multiply":
    print("what if your first number?")
    fifth_num = int(input())
    while fifth_num >= 500:
        print("the number is too high. what is your first number?")

    print("what is your second number?")
    sixth_num = int(input())
    while sixth_num >= 500:
        print("the number is too high. what is your second number?")
        sixth_num = int(input())

    multiply(fifth_num, sixth_num)

#for dividing sev_num and eig_num
if question == "divide":
    print("what is your first number?")
    sev_num = int(input())

    print("what is your second number?")
    eig_num = int(input())

    divide(sev_num, eig_num)


