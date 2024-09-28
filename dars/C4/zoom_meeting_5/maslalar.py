
class MyClass10:
    nums=[1,2,3,4,5,6,7,8,9,10]
    sum1=0
    def devide(self,d):
        for i in self.nums:
            if i%d==0:
                self.sum1+=int(i)
        return self.sum1
print(MyClass10.devide(MyClass10,5))