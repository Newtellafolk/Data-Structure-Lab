"""mox_mon"""
import json as j
def main():
    """mox_mon"""
    score = j.loads(input())
    total = len(score)
    mon = score[0]
    mox = score[0]

    for numm in score:
        if numm > mox:
            mox = numm
        if numm < mon:
            mon = numm

    avg = ((sum(score)) / total)
    result_avg = round(avg, 2)
    result_all = mox, mon, result_avg
    print(result_all)

main()
