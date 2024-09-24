class MyClass6:
    words=[]
    def add_word(self,word):
        self.words.append(word)
        print(self.words)
    def remove(self,word):
        self.words.remove(word)
        print(self.words)
MyClass6.add_word(MyClass6,"Olma")
MyClass6.remove(MyClass6,"Olma")