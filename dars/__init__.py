son=int(input("son kiriting: "))
sum=0
for i in range(1,son+1):
    if i%3==0 and i%9!=0:
        sum+=i
print(sum)