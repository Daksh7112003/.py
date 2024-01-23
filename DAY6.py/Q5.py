n = int(input("Enter the no"))
temp = n 
rev= 0 
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if rev==temp:
    print("Hell yes")
else:
    print("hell no")    
