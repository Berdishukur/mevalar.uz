import  random

find_number=random.randint(1,100)
jon=100
while True:
    taxminiy_son=int(input("Sonni kiriting : "))
    if taxminiy_son==find_number:
        print("Siz yutdingiz !!!")
        break
    elif taxminiy_son*2<=find_number:
        print("Juda past")
    elif taxminiy_son < find_number:
        print("Ozgina past")
    elif taxminiy_son>2*find_number:
        print("Juda baland")
    elif taxminiy_son>find_number:
        print("Ozgina baland")
    jon-=10
    print(f"Sizda {jon} ta jon qoldi")
    if jon==0:
        print("Siz yutqazdingiz .")
        break








#
# while True:
#     son1=int(input("Birinchi sonni kiriting : "))
#     amal=input("Amalni kiriting : ")
#     amallar=["-","+","/","*"]
#     while amal not  in amallar:
#         amal=input("Sizning amalingiz xato , qaytadan kiriting : ")
#     son2 = int(input("Ikkinchi sonni kiriting : "))
#     if amal=="+":
#         print("yig'indi = ",son1+son2)
#     elif amal=="-":
#         print("Ayirma = ",son1-son2)
#     elif amal=="*":
#         print("Ko'paytma = ",son1*son2)
#     elif amal=="/":
#         print("Bo'linma = ",son1/son2)
#     tanlov=int(input(" Yana amal bajarasizmi? \n     1 ==>> YES \n     0 ==>> NO ...."))
#     if tanlov ==0:
#         print("Xayr  salomat bo'ling : ")
#         break



















# def work_with_list(a) :
#     a.sort()
#     kichik=a[0]
#     new_list=[]
#     for i in a:
#         new_list.append(i*kichik)
#     print(new_list)
# myList=[3,8,11,88,67,222,64,92]
# work_with_list(myList)
#


# def add_right(a, b):
#     print(a+b)
# a=input(" A = ")
# b=input(" B = ")
# add_right(a,b)

# def digit_count_and_sum(word):
#     count=0
#     for i in word:
#         if i.isdigit():
#             count+=1
#     print(F" {count} ta raqam mavjud ekan.")
#
# matn=input("matnni kiriting : ")
# digit_count_and_sum(matn)





# def daraja4(a, b, c, d):
#     print(a**d)
#     print(b**d)
#     print(c**d)
# a=int(input(" A = "))
# b=int(input(" B = "))
# c=int(input(" C = "))
# d=int(input(" D = "))
# daraja4(a,b,c,d)









# myList=[1,2,3,4,5,6,7,8,9]
# def list_sum(myList):
#     sum=0
#     for i in myList:
#         sum+=i
#     print("nateja = ",sum)
#
# list_sum(myList)

# def find_letter_count(word,letter):
#     count=0
#     for i in word:
#         if i.lower()==letter.lower():
#             count+=1
#     print("nateja = ",count)
#
# matn=input("So'zni kiriting : ")
# harif=input("Harifni kiriting : ")
# find_letter_count(matn,harif)



# def find_max(a,b,c):
#     print("Eng katta son= ",max(a,b,c))
#
# a=int(input(" A = "))
# b=int(input(" B = "))
# c=int(input(" C = "))
# find_max(a,b,c)

































# def digit_count_and_sum(word):
#     sum=0
#     for i in word:
#         if i.isdigit():
#             sum+=int(i)
#     print("raqamlari Yigindisi = ",sum)
# matn=input("Ixtiyoriy matnni kiriting : ")
# digit_count_and_sum(matn)
#
# # while True:
#     son=int(input("Dasturdan foydalanishni xohlaysizmi?\n Yes ===>>1 \n No ====>>0\n ....."))
#     if son==1:
#         print("Salom !!! ")
#     elif son ==0:
#         print("Xayr salomat bo'ling !!")
#         break
#     else:
#         print("Tanlovingiz xato .")









# n=int(input("N sonini kiriting : "))
# i=1
# sum=0
# while i<=n:
#
#     if i%5==0:
#         break
#     print(i)
#     i+=1

# ism=input("Ismongizni kiriting : ")
# familiya=input("familiyangizni kiriting : ")
# yosh=int(input("Yoshingizni kiriting : "))
# def user_data(first_name,last_name,age):
#     print(F"Ism : {first_name}\nFamiliya : {last_name}\nYosh : {age}")
# user_data(ism,familiya,yosh)




# n=int(input("N sonni kiriting : "))
# def musbat_manfiy_tekshir(N):
#     if N>0:
#         print("Musbat")
#     elif N<0:
#         print("Manfiy")
#     else:
#         print("Nol")
# musbat_manfiy_tekshir(n)



# def juft_toq_tekshir(n):
#     if n % 2 == 0:
#         print("Juft")
#     else:
#         print("Toq")
#
# juft_toq_tekshir(n)








# def ayir(a,b):
#     return a-b
#
# x=int(input("birinchi sonni kiriting : "))
# y=int(input("Ikkinchi sonni kiriting : "))
#
# print(ayir(x,y))


# matn=input("Matn = ")
#
# def uzunlig(txt):
#     sum=0
#     for i in txt:
#         sum+=1
#     print(sum)
# uzunlig(matn)





















 # print(get_time(2024,2,2))


# suz=input("So'z kiriting : ")
# son=int(input("Sonni kiriting : "))
# yangi_suz=""
# for i in range(len(suz)):
#     if i==son:
#         continue
#     yangi_suz+=suz[i]
# print(yangi_suz)
# if 2>3:
#     pass
# else:
#     print("csdc")
#

# rang =["Qora","Oq","Yashil"]
# mashena=["Nexia","lasetti","gentira"]
# for i in rang:
#     for j in mashena:
#         print(i,j)



# for i in range(1,10):
#     print(i)
#     if i==3:
#         continue
# else:
#     print("Sikl tugadi")

# for i in range(7):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(1,11):
#     if i==7:
#         continue
#     print(i)






# for i in "dastur":
#
#     if i == 's':
#         break
#     print(i)
# for i in range(1,100):
#     print(i)
#     if i==10:
#         break



# for i in "S alom":
#     print(i)

# meva = ["olma", "anor", "banan"]
# for i in meva:
#     print(i)













#
#
#
#
#
#
#
#
# import json
#
# with open("test.json", 'r') as f:
#     json_to_python = json.load(f)
#
# for savol in json_to_python:
#     print(savol["question"])
#     javoblar = savol['answers']
#
#     variantlar = ['A', 'B', 'C', 'D']
#     for i, javob in enumerate(javoblar):
#         print(f"{variantlar[i]}) {javob['answers']}")
#
#     tanlov = input((f"A){javoblar[0]}\nB){javoblar[1]}\nC{javoblar[2]}\nD){javoblar[3]}\n   >>>>> "))
#     tanlangan_javob = javoblar[variantlar.index(tanlov.upper())]
#     if tanlov == "A" and javoblar[0][" isTrue"] == True:
#         print("Sizning javobingiz to'g'ri")
#     else:
#         print("Siz xato javob qaytardingiz")
#
#
#
#
#
#
# # foydalanuvchidan qiziqishlari so'ralsin.
# #
# # Agar kitob yoki kutubxona qiziqishlari orasida bo'lsa, qanday kitoblar yoqishi so'ralsin.
# #     agar detektiv so'zini ishlatsa, shaytanat kitobi haqidagi fikri so'ralsin.
# #     agar diniy kitoblarga qiziqsa "Hadis va Hayot" kitoblar to'plamini sovg'a qilamiz deyilsin.
# #
# # Agar sport so'zi qiziqishlari orasida bo'lsa, qaysi sport turiga qiziqishi so'ralsin,
# #    agar futbol sport turlari orasida bo'lsa, qaysi komandani yoqtirishi so'ralsin.
# #         agar real yoki barsa komandasini yozsa, el-classicoga chipta sovg'a qilamiz deyilsin
# # """
# #
# # qiziqish=input("Nimga qiziqasiz ? ")
# #
# # if "kitob" in qiziqish or "kutubxona" in qiziqish:
# #     kitob=input("Qanday kitoblarga qiziqasiz ? ")
# #     if "detektiv" in kitob:
# #         fikir=input("Shaytanat kitobi haqida fikringiz qanday ? ")
# #     elif "diniy" in kitob:
# #         print("Hadis va Hayot kitoblari sizga sovg'a")
#
#
# # elif "sport" in qiziqish:
# #     pass
# # else:
# #     print("Sizdagi qiziqishlar haqida bizda malumot yo'q")
# #
#
#
#
#
#
#
#
#
#
#
# # N=int(input("N  = "))
# # r1=str(N)[0]
# # r2=str(N)[1]
# # r3=str(N)[2]
# # r4=str(N)[3]
# #
# # if r1<r2<r3<r4:
# #     print("o'suvchi")
# # elif r1>r2>r3>r4:
# #     print("kamayuvchi")
# # else:
# #     print("tartibsiz")
#
#
# # N=int(input(" N= "))
# # if N%2==0:
# #     print(N**2)
# # else:
# #     print(N**3)
#
#
# # fuqoralik=input("Millatingizni kiriting : ")
# # yosh=int(input("Yoshingizni kiriting : "))
# #
# # if "uzb" in fuqoralik.lower() and yosh>=18:
# #     print('sizda saylash huquqi bor')
# # else:
# #     print("sizda saylash huquqi yo'q")
#
#
#
