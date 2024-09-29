name=input("Enter your good name here ")
print("Hello", name)
print("What you want to choose?")
options=int(input("\n1. Addition" "\n2. Subtraction" "\n3. Multiplication" "\n4. Division" "\n5. Exit"  ))

def switch_case(options):
    match  options:
        case 1:  
            a=int(input("Enter first number"))
            b=int(input("Enter second number"))
            print("Sum is: ", a+b)
        case 2:  
            a=int(input("Enter first number"))
            b=int(input("Enter second number"))
            print("Subtraction is: ", a-b)
        case 3:  
            a=int(input("Enter first number"))
            b=int(input("Enter second number"))
            print("Multiplication is: ", a*b)
        case 4:  
            a=int(input("Enter first number"))
            b=int(input("Enter second number"))
            print("Division is: ", a/b)
        case 5: 
            quit()
switch_case(options)
