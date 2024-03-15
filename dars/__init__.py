

nums=[1,1,1,2,2,4,4,4,4,4,5,7,7,]
reslut={}
def counter_dict(nums):
    for i in nums:
        reslut[i]=nums.count(i)
    print(reslut)
counter_dict(nums)



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

