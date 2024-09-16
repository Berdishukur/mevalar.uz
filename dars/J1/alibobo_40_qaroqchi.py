import  random
hudud=[
    ["*","*","*","*","*"],
    ["*","*","*","*","*"],
    ["*","*","*","*","*"],
    ["*","*","*","*","*"],
    ["*","*","*","*","X"],
]
def hudud_print():
    for i in hudud:
       print(i)


class Player:
    def __init__(self,x,y,health):
        self.health=health
        self.x=x
        self.y=y
    def go(self,dx,dy):
        hudud[self.y][self.x] = "*"
        self.x+=dx
        self.y+=dy
        if hudud[self.y][self.x] == "X":
            print("yutdingiz Tabrikalymiz")
            return 1
        elif hudud[self.y][self.x] == "#":
            player1.health -= dushman.kuch
            print(F"O'yinchining sog'ligi = {player1.health}")
            hudud[self.y][self.x] = "P"
        else:
            hudud[self.y][self.x]="P"


player1=Player(0,0,100)
hudud[player1.y][player1.x]="P"
hudud_print()
class Dushman(Player):
    def __init__(self,kuch):

        self.kuch=kuch
    def joylashuv(self):
        dx=random.randint(1,4)
        dy=random.randint(1,4)
        while hudud[dx][dy]!="*":
            dx = random.randint(1, 4)
            dy = random.randint(1, 4)

        if hudud[dx][dy]=="P":
            player1.health-=dushman.kuch
            print(F"O'yinchining sog'ligi = {player1.health}")
        hudud[dx][dy]="#"
dushman=Dushman(15)
dushman.joylashuv()


while True:
    x=int(input("Oldinga ==>>1 ,Orqaga ==>> -1, Joyida ==>> 0"))
    y=int(input("Pastga ==>>1 ,Tepaga ==>> -1, Joyida ==>> 0"))

    player1.go(x,y)
    hudud_print()
    dushman.joylashuv()
