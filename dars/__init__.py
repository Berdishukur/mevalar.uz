
nums=int(input("son kiriting: "))
nums1=str(nums)
num1=int(nums1[0])
num2=int(nums1[1])
num3=int(nums1[2])
num4=int(nums1[3])
if num1<num2<num3<num4:
    print("o'suvchi")
elif num4<num3<num2<num1:
    print("kamayuvchi")
else:
    print("tartibsiz")