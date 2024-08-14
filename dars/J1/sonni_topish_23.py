import random
x=random.randint(1,100)
count=0
jon=8
while True:
    print(F"Sizda {jon} ta jon bor . ")
    jon-=1
    tanlov=int(input("Tanlavingizni kiriting : "))
    count+=1
    if x==tanlov:
        print(f"Siz {count} marta o'ynashda  yutdingiz!!!")
        break
    elif jon==0:
        print("Sizning joningiz nolga teng bo'ldi \n     Xayr salomat bo'ling.")
        break
    elif tanlov>=2*x:
        jon-=1
        print("Juda baland")
    elif x<tanlov<2*x:
        jon+=1
        print("Ozgina balandroq")
    elif tanlov<=int(x/2):
        jon-=1
        print("Juda past")
    elif int(x/2)<tanlov < x:
        jon+=1
        print("Ozgina pastroq")
    else:
        print("Tanlovingiz xato")
    if  count%5==0:
        jon-=2


