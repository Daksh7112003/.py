
def printstar(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")

        print()

if __name__== "__main__":

    try:
                   
         n = int(input("ENter the number"))
         printstar(n)
    except ValueError:
      print("sjcbkjshkjh")
        
