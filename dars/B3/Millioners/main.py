from reyting_file import reyting,users
from uyin_file import uyin

while True:
    tanlov=int(input(f"""Kim millioner bo'lishni istaydi o'yiniga xush kelibsiz
         1 ==>> o'ynash
         2 ==>> reyting
         0 ==>> dasturdan chiqish.
             >>>....
    """))
    uyinlar_soni=0
    max_ball=0

    if tanlov==1:

        uyin()

    elif tanlov==2:
        reyting(users)
    elif tanlov==0:
        print("Xayr salomat bo'ling!!")
        break