g=["🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎"]

def jadval():
    print(F"""
    ---------------
    | {g[0]} | {g[1]} | {g[2]} | 
    ---------------
    | {g[3]} | {g[4]} | {g[5]} |
    ---------------
    | {g[6]} | {g[7]} | {g[8]} |
    ---------------
    """)
while True:
  x=int(input(" X = "))
  while g[x-1]=="X" or g[x-1]==0 :
   print("Bu katak band qaytadan kiriting : ")
   x = int(input(" X = "))
  g[x-1]="X"
  jadval()
  if g[0]==g[1]==g[2]=="X" or g[3]==g[4]==g[5]=="X" or g[6]==g[7]==g[8]=="X" or g[0]==g[3]==g[6]=="X" or g[1]==g[4]==g[7]=="X" or g[2]==g[5]==g[8]=="X" or g[0]==g[4]==g[8]=="X" or g[2]==g[4]==g[6]=="X":
   print("X yutdi ,Tamom.")
   break
  o=int(input(" 0 = "))
  while g[o-1]=="X" or g[o-1]==0 :
   print("Bu katak band qaytadan kiriting : ")
   o = int(input(" 0 = "))
  g[o-1]=0
  jadval()

