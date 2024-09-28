import  random
g=["🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎","🍎"]

# print(f"""
# {g[0]}| {g[1]}| {g[2]}
# {g[3]}| {g[4]}| {g[5]}
# {g[6]}| {g[7]}| {g[8]}
# """)
while True:
    x = random.randint(1,9)
    while g[x-1]=="🐍" or g[x-1]=="🐢":
        x = random.randint(1,9)
    g[x - 1] = "🐍"
    print(f""" 

    {g[0]}| {g[1]}| {g[2]}
    {g[3]}| {g[4]}| {g[5]}
    {g[6]}| {g[7]}| {g[8]}
    """)
    if g[0]==g[1]==g[2]=="🐍" or g[3]==g[4]==g[5]=="🐍" or g[6]==g[7]==g[8]=="🐍" or g[0]==g[3]==g[6]=="🐍" or g[1]==g[4]==g[7]=="🐍" or g[2]==g[5]==g[8]=="🐍" or g[0]==g[4]==g[8]=="🐍" or g[2]==g[4]==g[6]=="🐍" :
        print("🐍 Yutdi,tamom!!")
        break

    o = int(input("🐢  = "))
    while g[o - 1] == "🐢" or g[o-1]=="🐍":
        print("Bu joy band qaytadan kiriting..")
        o = int(input("🐢  = "))
    g[o - 1] = "🐢"
    print(f"""
    
                  {g[0]}| {g[1]}| {g[2]}
                  {g[3]}| {g[4]}| {g[5]}
                  {g[6]}| {g[7]}| {g[8]}
                  """)
    if g[0] == g[1] == g[2] == "🐢" or g[3] == g[4] == g[5] == "🐢" or g[6] == g[7] == g[8] == "🐢" or g[0] == g[3] == g[
        6] == "🐢" or g[1] == g[4] == g[7] == "🐢" or g[2] == g[5] == g[8] == "🐢" or g[0] == g[4] == g[8] == "🐢" or g[2] == g[
        4] == g[6] == "🐢":
        print("🐢 Yutdi,tamom!!")
        break


