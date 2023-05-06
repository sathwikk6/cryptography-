from random import randint
if __name__=='__main__':
    p=23
    g=9
    print('the value of p is :%d'%(p))
    print('the value of g is :%d'%(g))
    a=4
    print('the private key a for alice is :%d'%(a))
    x=int(pow(g,a,p))
    b=3
    print('the privatekey b for bob is :%d'%(b))
    y=int(pow(g,b,p))
    ka=int(pow(y,a,p))
    kb=int(pow(x,b,p))
    print('secret key for the alice is :%d'%(ka))
    print('secret key for the bob is : %d'%(kb))
