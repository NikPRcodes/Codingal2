import random
options = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a',
           's','d','f','g','h','j','k','l','z','x','c','v','b','n','m','!','@','%','&']
password = ''
characters = int(input("how many charaters does your password need to have? : "))
c = 0
while True:
    a = random.choice(options)
    password += a
    c += 1
    if c == characters:
        print("your password is " , password)
        break