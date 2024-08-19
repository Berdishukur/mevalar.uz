#     1. A soni berilgan. Uni musbat yoki manfiy ekanligini aniqlang

# A=8
# if A>0:
#     print("Musbat")
# elif A<0:
#     print("Manfiy")
# else:
#     print("Nol")

# 11. A, B va C sonlari berilgan. Ulardan nechtasi musbat ekanligni aniqlang.
# A=int(input(" A = "))
# B=int(input(" B = "))
# C=int(input(" C = "))
#
# if A>0 and B>0 and C>0:
#     print(3," ta musbat")
# elif A>0 and B>0 and  C<0 or A>0 and B<0 and C>0 or A<0 and B>0 and C>0:
#     print(2,"ta musbat")
#
# elif A>0 or B>0 or C>0:
#     print(1," ta musbat")
# else:
#     print("Musbat sonlar yo'q ")


# 12. A, B va C sonlari berilgan. Ulardan ikkita  eng katta sonlarni yig’indisini aniqlang.
#
# A=int(input(" A = "))
# B=int(input(" B = "))
# C=int(input(" C = "))
# if C<B<A or C<A<B:
#     print(A+B)
# elif B<C<A or B<A<C:
#     print(C+A)
# elif A<C<B or A<B<C:
#     print(B+C)
# else:
#     print("2 ta katta son yo'q")

# 14. A va B sonlari berilgan. A va B ni , yani ikkalasi ham tog’ sonlar ekanligini
# aniqlang


# A=int(input(" A = "))
# B=int(input(" B = "))
#
# if A%2==1 and B%2==1:
#     print(True)
# else:
#     print(False)

# 16. A, B va C sonlari berilgan. A, B va C sonlarini musbatmi shuni aniqlang.

# A=int(input(" A = "))
# B=int(input(" B = "))
# C=int(input(" C = "))
#
# if A>0 and B>0 and C>0:
#     print("Musbat")
# else:
#     print("Musbat emas")

# 17. A soni berilgan. Uni juft va 2 xonalik son ekanligni aniqlang.
#
# A=int(input(" A = "))
#
# if A%2==0 and 9<A<100:
#     print(True)
# else:
#     print(False)
g = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

print(f"""
             {g[0]} | {g[1]} | {g[2]}
             ----------
             {g[3]} | {g[4]} | {g[5]}
             ----------
             {g[6]} | {g[7]} | {g[8]}

""")
while True:
    x = int(input("x = "))
    while g[x - 1] == "x" or g[x - 1] == 0:
        print("Bu katak bant boshqasini kiriting !")
        x = int(input("X = "))
    g[x - 1] = "x"
    print(f"""                                       
             {g[0]} | {g[1]} | {g[2]}
             ----------
             {g[3]} | {g[4]} | {g[5]}
             ----------
             {g[6]} | {g[7]} | {g[8]}
""")
    if g[0] == "x" and g[1] == "x" and g[2] == "x" or g[3] == "x" and g[4] == "x" and g[5] == "x" or g[6] == "x" and g[7] == "x" and g[8] == "x" or g[0] == "x" and g[4] == "x" and g[8] == "x" or g[0] == "x" and g[
        3] == "x" and g[6] == "x" or g[1] == "x" and g[4] == "x" and g[7] == "x" or g[2] == "x" and g[5] == "x" and g[8] == "x" or g[2] == "x" and g[4] == "x" and g[6] == "x":
        print("x yutdi : xayir")
        break
    o = int(input("o = "))
    while g[o - 1] == "o" or g[o - 1] == 0:
        print("Bu katak bant boshqasini kiriting !")
        o = int(input("o = "))
    g[o - 1] = "o"
    print(f"""                                       
             {g[0]} | {g[1]} | {g[2]}
             ----------
             {g[3]} | {g[4]} | {g[5]}
             ----------
             {g[6]} | {g[7]} | {g[8]}
""")

    if g[0] == "o" and g[1] == "o" and g[2] == "o" or g[3] == "o" and g[4] == "o" and g[5] == "o" or g[6] == "o" and g[7] == "o" and g[8] == "o" or g[0] == "o" and g[4] == "o" and g[8] == "o" or g[0] == "o" and g[
        3] == "o" and g[6] == "o" or g[1] == "o" and g[4] == "o" and g[7] == "o" or g[2] == "o" and g[5] == "o" and g[8] == "o" or g[2] == "o" and g[4] == "o" and g[6] == "o":
        print("0 yutdi : xayir")
        break












