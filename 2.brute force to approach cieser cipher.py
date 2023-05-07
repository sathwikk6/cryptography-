message='UDZWKLVVLGH'
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(letters)):
    translated=""
    for ch in message:
        if ch in letters:
            num=letters.find(ch)
            num=num-key
            if num<0:
                num=num+len(letters)
            translated=translated+letters[num]
        else:
            translated=translated+ch
    print('hacking key is %s: %s' %(key,translated))   
