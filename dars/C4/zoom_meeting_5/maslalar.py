class Student:
    holat='uyqichi'
    def __init__(self,name="Anna",age=22,gender="Ayol"):
        self.name=name
        self.age=age
        self.gender=gender
        print("Work init")

talaba1=Student("Ali",25,"Erkak")
talaba2=Student(name="Aziz",gender="Erkak")
# print(talaba2.age)
print(talaba1.holat)
print(talaba2.holat)
Student.holat="Kitobxon"
print(talaba1.holat)










# class MyClass10:
#     nums=[1,2,3,4,5,6,7,8,9,10]
#     sum1=0
#     def devide(self,d):
#         for i in self.nums:
#             if i%d==0:
#                 self.sum1+=int(i)
#         return self.sum1
# print(MyClass10.devide(MyClass10,5))