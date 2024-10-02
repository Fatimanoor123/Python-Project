a=0
b=1
n=6
list=[]
for i in range(n):
    c=a+b
    list.append(a)
    a=b
    b=c
print(list)
