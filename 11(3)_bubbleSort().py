"""bubbleSort()"""
import json as js
def bubbleSort():
    lst = js.loads(input())
    last = int(input()) + 1
    count = 0
    currnt = 0
    sort = False

    while currnt <= last and sort == False:
        sort = True
        walker = last - 1
        
        while walker > currnt:
            if lst[walker] < lst[walker - 1]:
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
                sort = False
            count += 1
            walker -= 1
        print(lst)
        currnt += 1
    print("Comparison times: %d" %count)

bubbleSort()
