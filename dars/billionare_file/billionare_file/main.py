#  dars 24 Abduhamidov Shahzod

# Who wants to be billionere ?! 

from reyting_file import reyting, users
from uyin_file import uyin

while True:
    tanlov = int(input(f"""Kim millioner bo'lishni istaydi o'yiniga xush kelibsiz  !!!
                       O'yin o'ynashni boshlaymiz :
                           ==>>  Buyruqni tanlang :  <<==
                       1) ==>>  O'yinni boshlash     <<==
                       2) ==>>  Reytingni kurish     <<==
                                             
                       0  ==>>  Dasturdan chiqish  <<==
                       
                       
            Enter  ====>>>.......     """))
    uyinlar_soni = 0
    max_ball = 0
    if tanlov == 1:
        uyin()
    elif tanlov == 2:
        reyting(users)
    elif tanlov == 0:
        print(f"""Siz dasturni tark etmoqdasiz !!!
        Xayr salomat buling !!!
""")
        break
