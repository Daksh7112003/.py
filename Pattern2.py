

def starpattern(n):
    for i in range(n):
        for j in range(i+1): #i tak chalega yeh.....
            print("*",end=" ")

        print()  

if __name__=="__main__":
    n = int(input("Enter"))
    starpattern(n)
