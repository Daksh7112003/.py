
def countcharacters(sentence):
    digits=0
    uppercase=0
    lowercase=0
    for char in sentence:
        if char.isdigit():
            digits+=1
        elif char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
            

    return digits,uppercase,lowercase
    
if __name__=="__main__":

    sentence = input("Enter a input")
    digits,uppercase,lowercase=countcharacters(sentence)
    print(f"Number of digits: {digits}" )
    print(f"number of uppercase letters :{uppercase}" )
    print(f"dnmfjdsnh : {lowercase}")
    
