a=0
b=1
n = int(input("Enter the number"))
if n<0:
    print("Incorrect input")

elif n==1 :
    print(a)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c

    print(b)    

