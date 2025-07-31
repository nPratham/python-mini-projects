print("Welcome to the calculator program!")
while True:
    operation = input(f"which operation you wanna do with this number: eg.(add, sub, mul, div) ")
    if operation == "add":
        input1 = int(input("Enter your first number: "))
        input2 = int(input("Enter your second number: "))
        print(f"the addition of selected number is: {input1 + input2}")
        user_option = input("Do you want to continue? (yes/no): ")
        if user_option.lower() != "yes":
            print("Thank you for using the calculator program!")
            break
    elif operation == "sub":
        input1 = int(input("Enter your first number: "))
        input2 = int(input("Enter your second number: "))
        print(f"the substraction of selected number is: {input1 -input2}")
        user_option = input("Do you want to continue? (yes/no): ")
        if user_option.lower() != "yes":
            print("Thank you for using the calculator program!")
            break
    elif operation == "mul":
        input1 = int(input("Enter your first number: "))
        input2 = int(input("Enter your second number: "))
        print(f"the multiplication of selected number is: {input1*input2}") 
        user_option = input("Do you want to continue? (yes/no): ")
        if user_option.lower() != "yes":
            print("Thank you for using the calculator program!")
            break   
    elif operation == "div":
        input1 = int(input("Enter your first number: "))
        input2 = int(input("Enter your second number: "))
        if input2 ==0:
            print("we cannot divide numerator with 0!")
        input2 = int(input("Enter your second number: "))
        print(f"the division of selected number is: {input1 /input2}")
        user_option = input("Do you want to continue? (yes/no): ")
        if user_option.lower() != "yes":
            print("Thank you for using the calculator program!")
            break
    else:
        print("please take valid operation")