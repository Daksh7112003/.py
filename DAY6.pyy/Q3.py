#factorial...
fact=1
i=1
num=int(input("Enter the number" +" "))

if num<0:
    print("FBI")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of " ,  num ,"is ", fact)

