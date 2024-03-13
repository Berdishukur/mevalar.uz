

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

