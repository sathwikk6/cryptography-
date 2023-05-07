def decrypt(text,s):
    s=26-s 
    result=""  
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()): 
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result
word=str(input("enter the word:"))
d=int(input("Enter the key: "))
print("Encoded word in Caeser cipher is: ",decrypt(word,d))
