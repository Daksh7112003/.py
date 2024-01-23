#dictionary....


#left side is keys and right side is values ......
fruit={"Apple":10 , "Orange":20 , "Banana":40, "Carrot":70}
# print(fruit.keys())
#this will print the left side of the dictionary...

# print(fruit.values())
#this will print the right side of the dictionary .....


#for adding the element in the list...

fruit['mango']=200
# print(fruit)

#for changing the value of certain element , we can exchange it...


fruit['Apple']=90
# print(fruit)





#let suppose if we want to update the dictionary 
#from one to another......


fruit1={"hello":90,"car":8080}
# print(fruit1)


fruit2={"lii":8989,"kiji":6767}
fruit1.update(fruit2)


# print(fruit2)


#poping an element 
#just do fruit.pop()



fruit2.pop('kiji')
print(fruit2)