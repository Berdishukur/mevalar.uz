
# def salom_ber():
#     print("Hello")
# salom_ber()
# salom_ber()

# def salom_ber(ism):
#     print(f"Hello {ism}")
# salom_ber("Ali")
# salom_ber("G'ani")
# salom_ber("Salim")

# def daraja(son):
#     return  (son**2)
#
# print(daraja(7))

# def uzunlik(matn):
#     sum=0
#     for i in matn:
#         sum+=1
#     print(sum)
# uzunlik("salom")

# def ayirma(s1,s2):
#     return s1-s2
#
# result=ayirma(33,12)
# print("ayirma= ",result)

def find_max(a,b,c):
    if a>b>c or a>c>b:
        print(F"Eng katta son - A ={a}")
    elif b>a>c or b>c>a:
        print(F"Eng katta son - B ={b}")
    elif c>b>a or c>a>b:
        print(F"Eng katta son - C ={c}")
    elif a>=b>c:
        print(f"Eng katta son - A va B ={a}")
    elif a>=c>b:
        print(F"Eng katta son - A,C ={c}")
    elif c>=b>a:
        print(F"Eng katta son - B,C ={b}")
    elif a==b==c:
        print(F"Eng katta son - A,B,C ={a}")
son1=int(input("Son1 = "))
son2=int(input("Son2 = "))
son3=int(input("Son3 = "))
find_max(son1,son2,son3)




















