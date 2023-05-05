pip install rsa
import rsa
def generatekeys():
    (publickey,privatekey) = rsa.newkeys(1024)
    with open('keys/publckey.pem','wb') as p:
        p.write(publickey.save_pkcs1('PEM'))
    with open('keys/privatekey.pem','wb') as p:
        p.write(privatekey.save_pkcs1('PEM'))
def loadkeys():
    with open('keys/publickey.pem','rb') as p:
        publickey=rsa.publickey.load_pkcs1(p.read())
    with open('keys/privatekey.pem','rb') as p:
        privatekey=rsa.privatekey.load_pkcs1(p.read())
    return privatekey,publickey
def encrypt(message,key):
    return rsa.encrypt(message.encode('ascii'),key)
def decrypt(ciphertext,key):
    try:
        return rsa.decrypt(ciphertext,key).decode('ascii')
    except:
        return False
def sign(message,key):
    return rsa.sign(message.encode('ascii'),key,'SHA-1')
def verify(message,signature,key):
    try:
        return rsa.verify(message.encode('ascii'),signature,key,) =='SHA-1'
    except:
        return False
generatekeys()
publickey,privatekey=load_keys()
message=input("saveetha school of engineering")
ciphertext=encrypt(message,publickey)
signature=sign(message,privatekey)
text=decrypt(ciphertext,privatekey)
print(f'cipher text:{ciphertext}')
print(f'signature:{signature}')
if text:
    print(f'message text: {text}')
else:
    print(f'unable to decrypt the message.')
if text:
    print(f'message text: {text}')
else:
    print(f'unable to decrypt the message.')
    
        
        
        
    
