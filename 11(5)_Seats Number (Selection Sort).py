"""Seats Number (Selection Sort)"""

import json as js
def Selection_Sort():
    lst = js.loads(input())
    last = int(input())
    time = 0
    count = 0
    while True:
        if count == last:
            break
        sortt = count
        wordd = count + 1
        while True:
            if wordd > last:
                break
            word_w = lst[wordd]
            word_s = lst[sortt]
            if ord(word_w[0]) == ord(word_s[0]):
                if int(word_w[1:]) < int(word_s[1:]):
                    sortt = wordd
            elif ord(word_w[0]) < ord(word_s[0]):
                sortt = wordd
            wordd += 1
            time += 1
        lst[count], lst[sortt] =lst[sortt], lst[count]
        print(lst)
        count += 1
    print("Comparison times:", time)

Selection_Sort()
