# 1-masala Fuksiya qaytaradigan stringni katta harflarga o'tkazib beradigan dekorator yarating.
def convert_string_to_uppercase(func):
    def ref(str):
        string=func(str)
        print(string.upper())
    return ref

@convert_string_to_uppercase
def string_to_uppercase(str):
    string_in = input("string kiriting: ")
    return string_in

string_to_uppercase(str)