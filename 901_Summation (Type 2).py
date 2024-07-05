"""Summation (Type 2)"""
def summation_1(num):
    result = 0
    for i in range(1, num + 1):
        result += 1
        return result
    
def summation_2(num):
    result = num * (num + 1)//2
    return result
def main():
    num = int(input())
    print(summation_2(num))
main()
