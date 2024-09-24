
numbers=[1,2,3,4,5,6,7,8,9]
def min_max(numbers,max_num,min_num):
    if max_num==max(numbers):
        print(True)
    else:
        print(False)
    if min_num==min(numbers):
        print(True)
    else:
        print(False)
min_max(numbers,9,3)