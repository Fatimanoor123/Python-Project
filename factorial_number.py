
def fact(num):
   for i in range(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*(num-1)


def main():
    num=int(input("Enter a number to get factorial of number: "))
    print("Factorial of number is ", fact(num))

main()
