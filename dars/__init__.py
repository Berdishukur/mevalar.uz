
# 2. Kiritilgan belgilardan  parollar generatsiya qiladigan generator yarating.
#
#      M: input: abs        output: abs→asb→sab→sba→bas→bsa



# def parol_generator(harf):
#     if len(harf) == 1:
#         yield harf
#     else:
#         for i in range(len(harf)):
#             for parol in parol_generator(harf[:i] + harf[i+1:]):
#                 yield harf[i] + parol
#
# belgi=input("Belgi= ")
# par = parol_generator(belgi)
#
# parollar=[parol for parol in par]
# print(parollar)


# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#
#
# num =int(input("son= "))
# print(factorial(num))
#

# mahsulotlar = { 'Olma':10000, 'anor':22000, 'uzum':40000, 'Anjir':25000, 'shaftoli':30000 }
# unli=['a','i','o',"o'",'u','e']
# mevalar=[i for i, j in mahsulotlar.items() if i[0].lower() in unli]
# print(mevalar)
# ages = [5, 12, 17, 18, 24, 32]
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
# print(list(adults))
# for x in adults:
#   print(x)


# from functools import reduce
# n =int(input("n="))
# print(reduce(lambda x, y: x + y, range(1, n + 1)))
#

# string_it = ["strings", "with", "map"]
# print(list(map(str.upper, string_it)))
# summa = lambda a, b: a+b
# a=float(input("Sonni kiriting="))
# b=float(input("Sonni kiriting="))
# print(summa(a,b))
# LIST COMPREHENSION
# l1=[1,2,3]
# l2=['a','b','c']
# ls=zip(l2,l1)
# print(dict(ls))

# mevalar=['Olma','anor','gilos','shaftoli','Nok']
# unlilar=['u',"o'",'i','e','o','a']
#
# mevalar2=[i for i in mevalar if i[0].lower() in unlilar ]
# print(mevalar2)
# l = []
# for x in range(2):
#     for y in range(2):
#         l.append((x, y))
# print(l)
# print([(x,y) for x in range(2) for y in range(2)])
# mahsulotlar = {
#     'olma':10000,
#     'anor':22000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# mevalar=[meva for meva,narx in mahsulotlar.items() if narx>=20000 ]
# print(mevalar)
#




# nums=[1,2,3,4,5,6,7,8,9,12]
# juftlar=[i**2 for i in nums if i%2==0]
#
# print(juftlar)
# nums=[1,1,1,2,2,4,4,4,4,4,5,7,7,]
# reslut={}
# def counter_dict(nums):
#     for i in nums:
#         reslut[i]=nums.count(i)
#     print(reslut)
# counter_dict(nums)

# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# def merge_list(l1, l2):
#     if len(l1) != len(l2):
#         print("something wrong happen")
#     else:
#         ans = {}
#         for i in range(len(l1)):
#             ans[l1[i]] = l2[i]
#         print(ans, end=" ")
#
# merge_list(list_1, list_2)

# davlatlar={'Parij':'Fransiya','Pekin':'Xitoy','Seul':'Koreya','Vashington':'Amerika'}
# davlat=input("davalt nomini kiriting: ")
# if davlat in davlatlar.values():
#     for poytaxt,dav in davlatlar.items():
#         if dav==davlat:
#             print(poytaxt)
# else:
#     print("Bunday malumot yo'q")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# print(sum(mahsulotlar.values())/len(mahsulotlar))
# num=mahsulotlar['anor']
# for meva,narx in mahsulotlar.items():
#     print(sum())
# hafta_kunlari={1:"dushanba",2:'seshanba',3:'chorshanba',4:'payshanba',5:'juma',6:'shanba',7:'yakshanba'}
# def kunni_top(son):
#     for key,value in hafta_kunlari.items():
#         if son==key:
#             print(hafta_kunlari[son])
# son=int(input("son kiriting: "))
# kunni_top(son)

# mevalar=["shaftoli", "olma", "nok" ]
# meva_dict={}
# for meva in mevalar:
#     meva_dict[len(meva)]=meva
# print(meva_dict)

# number=int(input("Sonni kiriting: "))
# numbers=[]
# i=1
# while i<=number:
#     count=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count>2:
#         numbers.append(i)
#     i+=1
# print(numbers)

      # 10 - misol
# digit_count_and_sum(word) - bu funksiya "word"ni i
      # chidagi raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.
# def digit_count_and_sum(word):
#     count=0
#     for i in range(0,len(word)):
#         if word[i].isnumeric():
#             count+=int(word[i])
#         else:
#             count=count
#     print(count)
# matn=input("so'z kiriting: ")
#
# digit_count_and_sum(matn)

#    # 9 - misol
#work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list
# elementlariga ko'paytirib qiymatini o'zgartiradi va yangi listni print qilsin.
# list=[]
# a=[3,4,5,2,6,8,11]
# def work_with_list(a):
#     min_son=a[0]
#     for son in a:
#         if son<min_son:
#             min_son=son
#     for i in a:
#         list.append(i*min_son)
#     print(list)
# work_with_list(a)
  # 8-misol
# def tublarini_top(son1,son2):
#     tub_list=[]
#     for son in range(son1,son2+1):
#         count=0
#         for i in range(1,son+1):
#             if son%i==0:
#                 count+=1
#         if count==2:
#             tub_list.append(son)
#     print(tub_list)
#
# son1=int(input("son kiriting: "))
# son2=int(input("son kiriting: "))
# tublarini_top(son1,son2)
#

# def yosh_hisobla(ism,tugilgan_yil):
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")
#
# ism=input("Ism kiriting: ")
# t_yil=int(input("Tug'ilgan yilini kiriting: "))
# yosh_hisobla(ism,t_yil)
# def salom_ber(ism):
#     """
#     Salom beruvchi funksiya
#     :param ism:
#     :return:
#     """
#     print(f"Assalomu alaykum {ism.title()}")
# ism=input("Ismni kiriting: ")
# salom_ber(ism)
# print(salom_ber.__doc__)
# a=int(input('a='))
# b=int(input('b='))
# def daraja(a,b):
#     print(str(a)+str(b))
# daraja(a,b)

# text=input("So'z kiriting: ")
# count=0
# for i in range(0,len(text)):
#     if text[i]=="a" or text[i]=="A":
#         count+=1
# print(count)

# a=int(input("a="))
# sonlar=[]
# sum=0
# for i in range(2,a+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count>2:
#         sum+=i
# print(sum)

# a=int(input("a="))
# b=int(input("b="))
# sum=0
# for i in range(a,b+1):
#     sum+=(i**2)
# print(sum)

