# def l(a):
#     return  a+10
# y=l(20)
# print(y)
#
# x = lambda a : a + 10
# print(x(5))
# yigindi=lambda a,b:a+b
# print(yigindi(12,15))



def daraja(n):
    return n **2

numbers = [1, 2, 3, 4]
result = map(daraja, numbers)
print(list(result))

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
nateja=map(lambda x,y: x+y,l1,l2)
print(list(nateja))



