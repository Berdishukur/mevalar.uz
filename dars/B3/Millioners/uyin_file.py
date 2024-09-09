from  reyting_file import users
import json

def uyin():
    uyinlar_soni=0
    max_ball=0
    with open('test.json', 'r') as j_file:
        p_file = json.load(j_file)
    ism = input("Ismingizni kiriting : ")
    for x, y in users.items():
        if ism == x:
            uyinlar_soni = y[0]
    uyinlar_soni += 1
    j=1
    for i in p_file:
        print(f"  savol {j} \ 10")
        j+=1
        print(i["question"])
        print(f"A) {i['answers'][0]['key']}")
        print(f"B) {i['answers'][1]['key']}")
        print(f"C) {i['answers'][2]['key']}")
        print(f"D) {i['answers'][3]['key']}")
        javob=input(" Enter >>> ... ")
        if javob.upper()=="A" and i['answers'][0]['isTrue']==True:
            max_ball+=1
        elif javob.upper()=="B" and i['answers'][1]['isTrue']==True:
            max_ball+=1
        elif javob.upper()=="C" and i['answers'][2]['isTrue']==True:
            max_ball+=1
        elif javob.upper()=="D" and i['answers'][3]['isTrue']==True:
            max_ball+=1
        else:
            print(" Xato javob berdingiz ")
            break
    for x,y in users.items():
        if x==ism and max_ball<y[1]:
            max_ball=y[1]
    users[ism]=[uyinlar_soni,max_ball]
