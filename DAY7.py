#function in python.......

def hello():
    print("Heloo world")


hello()











def even_odd(x):
    if x/2==0:
        print(x, "is even")
    else:
        print(x,"is odd")

even_odd(3) 





l1=[5,6,7]
final_list=list(filter(lambda x:x%2!=0,l1))
print(final_list)

l2=[5,6,7]
final_list2=list(map(lambda x:x*2, l2))
print(final_list2)