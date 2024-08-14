yosh=int(input("Yoshingizni kiriting : "))
if yosh>=60:
    print("Siz pensiya yoshidasiz.")
elif 18<yosh<60:
    print("Siz ishlaydigan yoshdasiz")
elif 7<=yosh<=18:
    print("Siz maktab yoshidasiz")
elif 2<yosh<7:
    print("Siz bog'cha yoshidasiz")
else:
    print("Siz ona qaramog'idasiz")


# if yosh>=60:
#     print("Siz pensiya olishingiz mumukun")
# else:
#     print("Sizning yoshingiz yetmadi")


# son=int(input("Sonni kiriting : "))
#
# if son%2==0:
#     print(son+2)
# else:
#     print(son-2)













# import random
# x=random.randint(1,100)
# while True:
#     tanlov=int(input("Tanlavingizni kiriting : "))
#     if x==tanlov:
#         print("Siz yutdingiz!!!")
#         break
#     elif tanlov>=2*x:
#         print("Juda baland")
#     elif x<tanlov<2*x:
#         print("Ozgina balandroq")
#     elif tanlov<=int(x/2):
#         print("Juda past")
#     elif int(x/2)<tanlov < x:
#         print("Ozgina pastroq")
#     else:
#         print("Tanlovingiz xato")
#
#
#
#
# # sonlar=[4,1,0,5,33,66,7,2]
# # sonlar.sort()
# # print(sonlar[-1])