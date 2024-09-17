# 7. Sonlar berilgan A va B (A < B). A va B oraligida joylashgan sonlarni
# kamayish tartibida print qilin (A va B) shu oraliqqa kirmasin. Shu
# sonlarni sonini (uzunligini) print qiling

# A=int(input(" A = "))
# B=int(input(" B = "))
#
# for i in range(B-1,A,-1):
#     print(i)

# 4. 1 dan n gacha bo`lgan sonlarni kvadratlari yig`indisini toping.
# n=int(input(" N = "))
# sum=0
# for i in range(1,n):
#     sum+=i**2
# print(sum)
# 5. Soz kiritaman. Undan keyin 1 dan – sozni uzunligigacha bolgan son
# kiritishimni sorasin. Kiritilgan sonni tartibidagi harifni soz da olib
# tashlasin

# matn=input(" So'z kiriting : ")
# n=int(input("Son kiriting : "))
# new_matn=""
# for i in range(0,len(matn)):
#     if i!=n:
#         new_matn+=matn[i]
# print(new_matn)

import random
# r_son=random.randint(1,100)
#
# while True:
#     tanlov=int(input("Ixtiyoriy sonni kiriting : "))
#     if tanlov==r_son:
#         print("Siz yutdingiz!!")
#         break
#     elif tanlov*2<r_son:
#         print("Juda past")
#     elif tanlov<r_son:
#         print("Ozgina past")
#     elif tanlov>2*r_son:
#         print("Juda baland")
#     elif tanlov>r_son:
# #         print("Ozgina baland")
# element=random.choice(("Olma","Anor","Nok"))
# print(element)
# 10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga
# ko'paytirib qiymatini o'zgartiradi va listni print qilsin.
#
# def work_with_list(a):
#     new_a=[]
#     kichik_son=min(a)
#     for i in a:
#         new_a.append(i*kichik_son)
#     print(new_a)
#
# sonlar=[9,6,4,3,11,2,77]
#
# work_with_list(sonlar)
mevalar=["Nok","Olma","Olcha","Gilos"]
def str_counter(strs):
    str_dict={}
    for i in mevalar:
        str_dict[len(i)]=i
    print(str_dict)
str_counter(mevalar)
















# sonlar=[3,1,2,6,8,99,33,42]
# matn="ali vali salim"
# print(matn.title().capitalize())











