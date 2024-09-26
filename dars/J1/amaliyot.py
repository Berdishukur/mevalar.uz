
class MyClass7 :
    myDict={}
    def add_element(self,key,val):
        self.myDict[key]=val
        print(self.myDict)
    def update(self,key,val):
        self.myDict[key]=val
        print(self.myDict)

MyClass7.add_element(MyClass7,"Ali","+998901234567")
MyClass7.add_element(MyClass7,"Guzal","+998976543218")
MyClass7.update(MyClass7,"Ali","+998991234567")




















