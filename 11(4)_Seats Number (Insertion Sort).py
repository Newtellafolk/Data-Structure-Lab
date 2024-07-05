"""Seats Number (Insertion Sort)"""

import json as js
def Seats_Number():
    lst = js.loads(input())
    last = int(input())
    time = 0
    ccc = 1

    while ccc <= last:
        hold = lst[ccc]
        walker = ccc - 1
        while True:
            if walker < 0 or (ord(hold[0]) > ord(lst[walker][0])):
                break
            if hold[0] == lst[walker][0]:
                if int(hold[1:]) >= int(lst[walker][1:]):
                    break
            lst[walker + 1] = lst[walker]
            walker -= 1
            time += 1
        lst[walker + 1] = hold
        time += 1
        ccc += 1
        print(lst)
        if walker < 0:
            time -= 1
    print("Comparison times:", time)

Seats_Number()
