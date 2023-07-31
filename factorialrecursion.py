def factorial(n):
    if n==0:
        return 1 
    else:
        return n*factorial(n-1)
    


if __name__=="__main__":
    try:

        n=int(input("enter a number:"))
        if n<0:
            print("factorial doesnt exists")
        else:
            result=factorial(n)
            print(f"the factorial of {n} is {result}")
    except ValueError:


         print("invlaid input")
    
    
