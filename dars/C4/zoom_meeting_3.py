
 # 1. A soni berilgan. Uni musbat yoki manfiy ekanligini aniqlang.
# A=int(input("A sonni kiriting : "))
# if A>0:
#     print("Musbat")
# elif A<0:
#     print("Manfif")
# else:
#     print("Nol")

  # 2. A soni berilgan. Uni tog’ yoki juft ekanligni aniqlang.
# A=int(input("A sonni kiriting : "))
# if A%2==1:
#     print("Toq")
# else:
#     print("Juft")

# 5. A va B sonlari berilgan. Bu A > 3 va B <= 6 shartimizga to’g’ri keladimi yoki
# yoqmi aniqlang.
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
# if A>3 and B<=6:
#     print(True)
# else:
#     print(False)

# 7. A va B sonlari berilgan. Ulardan birinchi katta keyin kichikgini print qiling.
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
# if A>B:
#     print(A,B)
# elif A<B:
#     print(B,A)
# else:
#     print("Sonlar teng")

# 8. A va B sonlari berilgan (float tipida). Ularning qaysi birida qo’ldiq qismi kichik
# bo’lsa shu sonni aniqlang.
# A=float(input("A sonni kiriting : "))
# B=float(input("B sonni kiriting : "))
# A_qoldiq=A-int(A)
# B_qoldiq=B-int(B)

# 10. A, B va C sonlari berilgan. B soni, A va C ni o’rtasidami yoki yoq aniqlang.
# A=float(input("A sonni kiriting : "))
# B=float(input("B sonni kiriting : "))
# C=float(input("C sonni kiriting : "))
# if (A+C)/2==B:
#     print(True)
# else:
#     print(False)

     # 11. A, B va C sonlari berilgan. Ulardan nechtasi musbat ekanligni aniqlang
#
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
# C=int(input("C sonni kiriting : "))
# if A>0 and B>0 and C>0:
#     print("3 ta musbat")
# elif (A >0 and B>0) or (A>0 and C>0) or (B>0 and C>0):
#     print("2 ta musbat")
# elif A>0 or B>0 or C>0:
#     print("1 musbat")
# else:
#     print("Musbat son yo'q")

# 12. A, B va C sonlari berilgan. Ulardan ikki eng katta sonlarni yig’indisini aniqlang.
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
# C=int(input("C sonni kiriting : "))
#
# if A>B>C or B>A>C:
#     print(A+B)
# elif A>C>B or C>A>B:
#     print(A+C)
# elif C>B>A or B>C>A:
#     print(B+C)
# else:
#     print("2 ta katta son mavjud emas ")

# 14. A va B sonlari berilgan. A va B ni , yani ikkalasi ham tog’ sonlar ekanligini
# aniqlang
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
#
# if A%2==1 and B%2==1:
#     print(True)
# else:
#     print(False)

# 16. A, B va C sonlari berilgan. A, B va C sonlarini musbatmi shuni aniqlang
# A=int(input("A sonni kiriting : "))
# B=int(input("B sonni kiriting : "))
# C=int(input("C sonni kiriting : "))
# if A>0 and B>0 and C>0:
#     print(True)
# else:
#     print(False)
# 17. A soni berilgan. Uni juft va 2 xonalik son ekanligni aniqlang.
# A=int(input("A = "))
# if A%2==0 and 9<A<100:
#     print(True)
# else:
#     print(False)
# 19. Uch xonalik son berilgan. Uning raqamlari bir xil emasligni aniglang.

# A=int(input("A = "))
# A_str=str(A)
# if A_str[0]!=A_str[1]!=A_str[2]:
#     print(True)
# else:
#     print(False)
#
# 20. 1-999 ga son berilgan. Uni musbat yoki manfiyligni va nechi xonaligini
# aniqlang.
#
# A=int(input("A = "))
# if A>0:
#     print("Musbat")
#     if 0<A<10:
#         print("Bir xonali")
#     elif 9<A<100:
#         print(" Ikki xonali")
#     elif 99<A<1000:
#         print("Uch xonali")
#     else:
#         print("Oraliqga mos son kiritmadingiz.")
# else:
#     print("Oraliqga mos son kiritmadingiz.")

# 23. X va Y sonlari berilgan. Bu sonlar koordinata o’qining qaysi chorakgida
# ekanligni aniqlang.
# X=int(input("X = "))
# Y=int(input("Y = "))
# if X>0 and Y>0:
#     print("1-chorak")
# elif X<0 and Y>0:
#     print("2- chorak")
# elif X<0 and Y<0:
#     print("3 -chorak")
# elif X>0 and Y<0:
#     print("4-chorak")
# else:
#     print("Son o'qida yoki markazda joylashgan")

# 21. Uch xonalik son berilgan. Uning raqamlari o’sish yoki kamayish tartibidami
# aniqlang.

# A=int(input("3 xonali sonni kiriting : "))
# A_str=str(A)
# if A_str[0]<A_str[1]<A_str[2]:
#     print("O'suvchi")
# elif A_str[0]>A_str[1]>A_str[2]:
#     print("Kamayuvchi")
# else:
#     print("tartibsiz")
    # 10- dars
# 2. 1 dan n gacha bo`lgan toq sonlar yig`indisini toping.

# n=int(input(" N = "))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
#
# print(sum)
#
# sonlar=(1,2,3,4,5,6,7,8,9,10)
# sum=0
# for son in sonlar:
#     sum+=son
#
# print(sum)

# yosh=22
# yosh=23
# print(yosh)

son=int(input("1 kg konfet narxini kiriting "))
for i in range(1,11):
    print(i/10*son)













































































































