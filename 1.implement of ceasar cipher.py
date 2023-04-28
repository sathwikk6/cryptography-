def encrypt_text(plaintext,n):
    ans=""
    for i in range(len(plaintext)):
        ch=plaintext[i]
        if ch=="":
            ans+=" "
        elif(ch.isupper()):
            ans+=chr((ord(ch)+n-65)%26+65)
        else:
            ans+=chr((ord(ch)+n-97)%26+97)
    return ans

plaintext="HELLOEVERYONE"
n=3
print("plain text is:"+ plaintext)
print("shift pattern is:"+ str(n))
print("cipher text is:" + encrypt_text(plaintext,n))
    
