import json

with open("test.json","r")as start_json:
    a=json.load(start_json)

def test():
    for i in a:
        b = list(i.values())
        yield b[0]

savollar = test()

def variant():
    for i in a:
        b = list(i.values())
        for y in b[1]:
            yield y["key"]

variant = variant()

def uyin_qismi():
    ism = str(input("Ismingiz: "))
    urinishlar = 0
    n = 1
    ball = 0
    while True:
        print(f"{n}.", next(savollar), "\n")
        print("a)", next(variant))
        print("b)", next(variant))
        print("c)", next(variant))
        print("d)", next(variant))
        print("\n")
        javob = str(input("Javobingiz: "))

        # B va c ni olish
        b = {"a": a[n - 1]["answers"][0],
             "b": a[n - 1]["answers"][1],
             "c": a[n - 1]["answers"][2],
             "d": a[n - 1]["answers"][3]}

        if javob in b:
            c = b[javob]
        else:
            print("Noto'g'ri javob!")

        n += 1
        urinishlar += 1
        if urinishlar == 10:
            break
        if javob in ["a", "b", "c", "d"] and c["isTrue"] == True:
            print("To'gri")
            ball += 1

        else:
            print("Noto'g'ri")

    with open("ishtirokchi.json", "r") as read_file:
        o = json.load(read_file)
        s = o.copy()
        for i in s:
            if i["ism"] == ism and i["max ball"] < ball:
                i["max ball"] = ball
                i["urinishlar soni"] += 1
            elif i["ism"] == ism and i["max ball"] >= ball:
                i["urinishlar soni"] += 1

        s.append({"ism":ism,"max ball":ball,"urinishlar soni":1})
    n = json.dumps(s,indent=4)
    t = open("ishtirokchi.json","w")
    t.write(str(n))
    t.close()


while True:
    tanlov = str(input("Buyruqni tanlang\n1-o'ynash\n2-reyting\n0-dasturdan chiqish\nnimani tanlaysiz: "))
    while True:
        if tanlov in ["0","1","2"]:
            break
        else:
            tanlov = str(input("Buyruqni tanlang\n1-o'ynash\n2-reyting\n0-dasturdan chiqish\nnimani talles: "))

    if tanlov == "0":
        break

    elif tanlov == "2":
        with open("ishtirokchi.json", "r") as read_file:
            b = json.load(read_file)
            print(b)

    elif tanlov == "1":
        uyin_qismi()


