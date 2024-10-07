xonlar=[1,2,3,4,5,6,7,8,9,10]
xonlar_holati=("Ekonamik","Standart","Luks")
mehmonlar={xonlar[1]:["Berdi",xonlar_holati[1]]}
def mehmonlarni_chiqar():
    print("|------------------|-------------------|-------------|")
    print(f"| Xona raqami      |   Ismi            |  xona holati|")
    for kalit, qiymat in mehmonlar.items():
        print("|------------------|-------------------|-------------|")
        print(f"| {kalit}                |  {qiymat[0]}               {qiymat[1]}           ")
    print("|------------------|-------------------|-------------|")
def mehmon_add():
    band_xonalar = list(mehmonlar.keys())
    ism = input("Ismingiz kiriting : ")
    xona_raqami = int(input("Xona raqamini kiriting :"))
    while xona_raqami in band_xonalar:
        print("Bu xona band ")
        xona_raqami = int(input("Xona raqamini kiriting :"))

    xona_holati = int(input(f"""
    Xona holatini tanlang...
        0 ==>> Ekonomika  
        1 ==>> Standart  
        2 ==>> Luks
    """))
    mehmonlar[xona_raqami] = [ism, xonlar_holati[xona_holati]]
    print(f"{ism} >> mehmonlar ro'yxatiga qo'shildi.")
while True:
    tanlov=int(input("""
    1 ==>> Mehmonlar ro'yxati  
    2 ==>> Mehmon qo'shish  
    3 ==>> Mehmonni chiqarish  
    
    0 ==>> Dasturdan chiqish  
    """))
    if tanlov==1:
        mehmonlarni_chiqar()
    elif tanlov==2:
        mehmon_add()
    elif tanlov==3:
        print("Bu menyu kuchga kirmagan")
    elif tanlov==0:
        print("Thanks you bro !!!")
        break
    else:
        print("Tanlovingiz xato  ")


