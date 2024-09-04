reyting={"Ali":[2,7]}
import json
with open("test.json","r") as f:
    json_to_python=json.load(f)
print(json_to_python)

while True:
    n=int(input("Kim millioner bo'lishni xohlaydi ? \n    1 ==>> o'ynash\n    2 ==>> reyting\n    0 ==>> Dasturdan chiqish\n    >>>>>..."))
    uyinlar_soni = 0
    if n==1:
        ism =input("O'yinchini ismini kiriting : ")
        for x,y in reyting.items():
            if x==ism:
                uyinlar_soni+=y[0]
        uyinlar_soni+=1
        max_ball=0
        for i in json_to_python:
            print(i["question"])
            print(f"A) {i['answers'][0]['key']}")
            print(f"B) {i['answers'][1]['key']}")
            print(f"C) {i['answers'][2]['key']}")
            print(f"D) {i['answers'][3]['key']}")
            javob=input(" Enter >>>>...")
            if javob.lower()=="a" and i['answers'][0]["isTrue"] ==True:
                max_ball+=1
            elif javob.lower()=="b" and i['answers'][1]["isTrue"] ==True:
                max_ball+=1
            elif javob.lower()=="c" and i['answers'][2]["isTrue"] ==True:
               max_ball+=1
            elif javob.lower()=="d" and i['answers'][3]["isTrue"] ==True:
                max_ball+=1
            else:
                break
        for x,y in reyting.items():
            if x==ism and max_ball<y[1]:
                max_ball=y[1]

        reyting[ism]=[uyinlar_soni,max_ball]
        with open('myfile.json', 'w', encoding='utf8') as json_file:
            json.dump(reyting, json_file, allow_nan=True,indent=4)
    elif n==2:
        print("|----------+---------------+---------|")
        print("|Name      |o'yinlar soni  |max ball |")
        print("|----------+---------------+---------|")
        for key,value in reyting.items():
            print(f"|{key.center(10)}|{value[0]}              | {value[1]}       |")
        print("|----------+---------------+---------|")

    elif n==0:
        print("Xayr salomat bo'ling!!!")
        break
    else:
        print('Tanlovingiz xato, qaytadan kiriting')