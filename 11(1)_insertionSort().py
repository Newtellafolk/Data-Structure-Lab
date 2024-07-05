"""insertionSort()"""
import json as js
def insertionsort():
    lst = js.loads(input())
    last_index = int(input())
    count = 0
    for i in range(1, last_index + 1):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
            count += 1
        if key >= lst[j] and j != -1:
            count += 1
        lst[j+1] = key
        print(lst)
    print("Comparison times: %d" %count)

insertionsort()
