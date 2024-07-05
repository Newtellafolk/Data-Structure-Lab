"""Seats Number (Bubble Sort)"""
import json as js
def bubble():
    lst = js.loads(input())
    last = int(input())
    countt = 0
    status = False
    time = 0
    while countt <= last and status is False:
        www = last
        status = True
        while www > countt:
            if ord((lst[www])[0]) == ord((lst[www - 1])[0]):
                if int((lst[www])[1:]) < int((lst[www - 1])[1:]):
                    status = False
                    lst[www], lst[www - 1] = lst[www - 1], lst[www]
            elif ord((lst[www])[0]) < ord(lst[www - 1][0]):
                status = False
                lst[www], lst[www - 1] = lst[www - 1], lst[www]
            time += 1
            www -= 1
        print(lst)
        countt += 1
    print("Comparison times:", time)

bubble()
