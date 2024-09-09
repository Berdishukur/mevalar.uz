users = {"Sevara       ": [3, 8], "Shahzod     ": [2, 6], "Alibek         ": [5, 9]}


def reyting(users):
    print("|************|*********|**********|")
    print("| Name         | Played   | max_ball|")
    print("|************|*********|**********|")
    for x, y in users.items():
        print(f"| {x.center(10)}| {y[0]}            | {y[1]}              |")
        print("|************|*********|**********|")
