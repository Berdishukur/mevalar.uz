
xonalar=[1,2,3,4,5,6,7,8,9,10]
xona_holatlari=("Ekonomik","Standart","Luks")
mehmonlar={xonalar[0]:["Ali",xona_holatlari[0]],xonalar[3]:["Vali",xona_holatlari[2]]}

def mehmonlarni_chiqar():
    print("|------------------|-------------------|-------------|")
    print(f"| Xona raqami      |   Ismi            |  xona holati|")
    for kalit, qiymat in mehmonlar.items():
        print("|------------------|-------------------|-------------|")
        print(f"| {kalit}                |  {qiymat[0]}               {qiymat[1]}           ")
    print("|------------------|-------------------|-------------|")

while True:
    buyruq=int(input(f"""
    1 ==>> Mehmonlar ro'yxati
    2 ==>> Mehmon qo'shish
    3 ==>> Mehmonni chiqarish

    0 ==>> Dasturdan chiqish
    """))
    if buyruq==1:
        mehmonlarni_chiqar()
    elif buyruq==2:
        print("Bu buyruq kuchga kirmagan")
    elif buyruq==3:
        print("Bu buyruq kuchga kirmagan")
    elif buyruq==0:
        print("Dasturdan foydalanganingiz uchun rahmat!!! ")
        break
    else:
        print("Bunday buyruq yo'q,qaytadan kiriting.")
