import random

maydon = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]
maydon[9][9] = "Soqqa"

dushman_kordinatalari = []


class Player:
    def __init__(self, nomi):
        self.nomi = nomi
        self.jon = 100
        self.qurol = 10
        self.dx = 0
        self.dy = 0

    def set_joylashuv(self):
        maydon[self.dy][self.dx] = "P"

    def update_joylashuv(self, a, b):
        maydon[self.dx][self.dy] = "."
        self.dy += a
        self.dx += b

    def get_name(self):
        return f"{self.nomi}"


class Dushman(Player):
    def __init__(self, name):
        super().__init__(name)
        self.qurol = random.randint(10, 35)

    def set_joylashuv(self, n):
        for i in range(n):
            self.dx = random.randint(0, 9)
            self.dy = random.randint(0, 9)
            while self.dx == 9 and self.dy == 9:
                self.dx = random.randint(1, 9)
                self.dy = random.randint(1, 9)
            maydon[self.dx][self.dy] = "#"
            dushman_kordinatalari.append([self.dx, self.dy])

    def update_joylashuv(self, n):
        a, b = 0, 0
        n = len(dushman_kordinatalari)
        for i in range(n):
            a = dushman_kordinatalari[i][0]
            b = dushman_kordinatalari[i][1]
            maydon[a][b] = "."

        dushman_kordinatalari.clear()
        for i in range(n):
            self.dx = random.randint(0, 9)
            self.dy = random.randint(0, 9)
            while self.dx == 9 and self.dy == 9:
                self.dx = random.randint(1, 9)
                self.dy = random.randint(1, 9)
            maydon[self.dx][self.dy] = "#"
            dushman_kordinatalari.append([self.dx, self.dy])


class QurolAnjomlar:
    def __init__(self, nomi):
        self.plus = 30
        self.minus = random.randint(10, 35)
        self.dx = 0
        self.dy = 0

    sumka = []

    def joylashtirish(self, n):
        omad = random.randint(1, 15)
        if omad % 2 == 0:
            for i in range(n):
                self.dx = random.randint(0, 9)
                self.dy = random.randint(0, 9)
                while self.dx == 9 and self.dy == 9:
                    self.dx = random.randint(1, 9)
                    self.dy = random.randint(1, 9)
                maydon[self.dx][self.dy] = "(+)"


def yangilash():
    # Har yurishda dushman ortib borishi uchun
    # Buni shunchaki o'chirib qoyish mumkun
    d1.set_joylashuv(2)
    dori.joylashtirish(1)
    is_jang, is_dori = 0, 0

    if maydon[p1.dx][p1.dy] == "(+)":
        if (p1.jon + dori.plus) <= 70:
            p1.jon += dori.plus
            is_dori = 1
        elif (p1.jon + dori.plus) > 70:
            p1.jon = 100
            is_dori = 1
    if maydon[p1.dx][p1.dy] == "#":
        p1.jon -= d1.qurol
        d1.jon -= p1.qurol
        if p1.jon <= 0:
            p1.jon = 0
        if d1.jon <= 0:
            d1.jon = 0
        is_jang = 1
    maydon[p1.dx][p1.dy] = "P"
    for i in range(10):
        for j in range(10):
            print(maydon[i][j], end="    ")
        print("\n")
    print(f"{p1.get_name()} joni: {p1.jon}            {d1.get_name()} joni: {d1.jon}")
    print(f"{p1.get_name()} qurol kuchi: {p1.qurol}     {d1.get_name()} zarba kuchi: {d1.qurol}")
    print(" ")
    if is_jang == 1:
        print(f"(#) Jang bo'ldi: -{d1.qurol} (#)")
    elif is_dori == 1:
        print(f"(+) Aspirin qabul qilindi: +{dori.plus} (+)")


p1 = Player("Mimi")
d1 = Dushman("Qaroqchi")
dori = QurolAnjomlar("Aspirin")
qurol = QurolAnjomlar("Chaqmoq")
# bag = QurolAnjomlar("Sumka")
print(""" 
   P -> o'yinchi
   # -> dushman
   (+) -> qoshimcha jon
   Harakatlanish: 2- pastga  8- tepaga
                  4- chapga  6- o'ngga
   Dushmanlar joylashuvini randomtarzda istalgan joyga ozgartiradi!
   Har yurishda dushmanlar soni 2 taga ortib boradi.
   Aspirinlar istalgan joyda paydo bo'ladi.
""")
dushman = int(input("Dushmanlar soni(2 dan 15 gacha): "))
d_soni = list(range(2, 16))
while dushman not in d_soni:
    print("Xato! Qayta kiriting.")
    dushman = int(input("Dushmanlar soni(2 dan 15 gacha): "))
d1.set_joylashuv(dushman)
p1.set_joylashuv()
yangilash()

while True:
    yurish = int(input("Yuring( <4/6>  v2/8^ ) > "))
    yurishlar = [2, 4, 6, 8]
    while yurish not in yurishlar:
        print("Xato yurish! Qayta kiriting.")
        yurish = int(input("Yuring( <4/6>  v2/8^ ) > "))

    if yurish == 4:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv(dushman)
        p1.update_joylashuv(-1, 0)
        yangilash()
        if p1.dx == 9 and p1.dy == 9:
            print("Yutdingiz! Tamom.")
            break

    elif yurish == 6:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv(dushman)
        p1.update_joylashuv(1, 0)
        yangilash()
        if p1.dx == 9 and p1.dy == 9:
            print("Yutdingiz! Tamom.")
            break

    elif yurish == 2:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv(dushman)
        p1.update_joylashuv(0, 1)
        yangilash()
        if p1.dx == 9 and p1.dy == 9:
            print("Yutdingiz! Tamom.")
            break

    elif yurish == 8:
        if p1.jon <= 0:
            print("Afsus yutqazdingiz!")
            break
        d1.update_joylashuv(dushman)
        p1.update_joylashuv(0, -1)
        yangilash()
        if p1.dx == 9 and p1.dy == 9:
            print("Yutdingiz! Tamom.")
            break