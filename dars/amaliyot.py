def the_tower_of_hanoi(n,a,b,c):
   if n==1:
       print(f"{n}chi halqani {a} dan {c} ga joylashtir!")
       return
   the_tower_of_hanoi(n-1,a,b,c)
   print(f"{n}chi halqani, {a},dan,{c}, ga joylashtir!")
   the_tower_of_hanoi(n - 1, b,c,a)
n=int(input("son kiriting>>>"))
the_tower_of_hanoi(n, 'a', 'c' ,'b')