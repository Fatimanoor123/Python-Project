num=int(input("Enter a numnber to check whether it is palindrome or not: "))
palin_num=0
while num>0:
    last_digit= num%10
    palin_num=palin_num*10+ last_digit
    num = num//10
if num == palin_num:
    print("Number is palindrome")
else:
    print("Number is not Palindrome")
