
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
def mehmon_add():
    ism = input("Ismini kiriting : ")
    xona_raqami = int(input("Xona raqamini kiriting (1-10) : "))
    band_xonalar = list(mehmonlar.keys())
    while xona_raqami in band_xonalar:
        print("Bu xona band, qaytadan kiriting")
        xona_raqami = int(input("Xona raqamini kiriting : "))
    xona_holati = int(input("      Xona holatini tanlang\nEkonamik ==>> 0.."
                            "\nStandart ==>> 1..\nLuks ==>> 2.."))
    mehmonlar[xonalar[xona_raqami - 1]] = [ism, xona_holatlari[xona_holati]]
    print(f"{ism} mehmonlar ro'yxatiga qo'shildi")


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
        mehmon_add()
    elif buyruq==3:
        print("Bu buyruq kuchga kirmagan")
    elif buyruq==0:
        print("Dasturdan foydalanganingiz uchun rahmat!!! ")
        break
    else:
        print("Bunday buyruq yo'q,qaytadan kiriting.")
