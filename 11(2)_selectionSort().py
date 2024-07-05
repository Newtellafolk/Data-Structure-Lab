"""selectionSort()"""

def selectionSort(lst, last):
    comparisons = 0
    for currt in range(last):
        smallst = currt

        for walker in range(currt + 1, last + 1):
            if lst[walker] < lst[smallst]:
                smallst = walker
            comparisons += 1

        lst[currt], lst[smallst] = lst[smallst], lst[currt]
        print(lst)

    print("Comparison times:", comparisons)

data = input()
data = list(map(int, data[1:-1].split(', ')))
last_index = int(input())

selectionSort(data, last_index)
