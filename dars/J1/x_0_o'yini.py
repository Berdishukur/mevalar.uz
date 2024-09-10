g=["🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎"]

import  random
def jadval():
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
while True:
    o=random.randint(1,9)
    print()
    while g[o-1]=="🐢" or g[o-1]=="🐍":
        o =random.randint(1,9)
    g[o-1]="🐢"
    jadval()
    if g[0]==g[1]==g[2]=="🐢" or g[3]==g[4]== g[5]=="🐢" or g[6]==g[7]==g[8]=="🐢" or g[0]==g[3]==g[6]=="🐢" or g[1]== g[4]== g[7] =="🐢" or g[2]== g[5]== g[8] =="🐢" or g[0]== g[4]== g[8]=="🐢" or g[2]== g[4]== g[6]=="🐢":
        print('0 yutdi! tamom')
        break


    x=int(input("X = "))
    while g[x-1]=='🐢' or g[x-1]=="🐍":
        print("Bu katak band qaytadan kiriting: ")
        x = int(input("X = "))
    g[x - 1] = "🐍"
    jadval()
    if g[0]==g[1]==g[2]=="🐍" or g[3]==g[4]== g[5]=="🐍" or g[6]==g[7]==g[8]=="🐍" or g[0]==g[3]==g[6]=="🐍" or g[1]== g[4]== g[7] =="🐍" or g[2]== g[5]== g[8] =="🐍" or g[0]== g[4]== g[8]=="🐍" or g[2]== g[4]== g[6]=="🐍" :
        print("X yudti. Xayr!!")
        break













