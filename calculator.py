#show user about options

print("Welcome to Calculator")
print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division ")
number=int(input("Select your option"))
 match number:
     case 1:
      num1=int(input("Enter first number"))
      num2=int(input("Enter Second number"))
      final= num1+num2
      print("The Sum of two number is", final)
     case 2:
        num1=int(input("Enter first number"))
        num2=int(input("Enter Second number"))
        final= num1-num2
        print("The Subtraction of two number is", final)
     case 3:
        num1=int(input("Enter first number"))
        num2=int(input("Enter Second number"))
        final= num1*num2
        print("The multiplication of two number is", final)
     case 4:
        num1=int(input("Enter first number"))
        num2=int(input("Enter Second number"))
        final= num1/num2
        print("The Sum of two number is", final)
    
    
    