g=[1,2,3,4,5,6,7,8,9]


print(f"""
             {g[0]} | {g[1]} | {g[2]} 
            -----------
             {g[3]} | {g[4]} | {g[5]}
            -----------
             {g[6]} | {g[7]} | {g[8]} 
"""
      )

while True:
    x=int(input("X = "))
    while g[x-1]=='X' or g[x-1]==0:
        print("Bu katak band qaytadan kiriting: ")
        x = int(input("X = "))
    g[x - 1] = "X"
    print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
          )
    if g[0]=="X" and g[1]=="X" and g[2]=="X" or g[3]=="X" and g[4]=="X" and g[5]=="X" or g[6]=="X" and g[7]=="X" and g[8]=="X" or g[0]=="X" and g[3]=="X" and g[6]=="X" or g[1]=="X" and g[4]=="X" and g[7] =="X" or g[2]=="X" and g[5]=="X" and g[8]=="X" or g[0]=="X" and g[4]=="X" and g[8]=="X" or g[2]=="X" and g[4]=="X" and g[6]=="X" :
        print("X yudti. Xayr!!")
        break
















