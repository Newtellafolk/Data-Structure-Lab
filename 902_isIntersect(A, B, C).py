"""isIntersect(A, B, C)"""
def intersect_check(a, b, c):
    for member_a in a:
        if member_a in b and member_a in c:
            return True
    return False

aaa = input()
bbb = input()
ccc = input()

a = [int(x) for x in aaa[1:-1].split(',')]
b = [int(x) for x in bbb[1:-1].split(',')]
c = [int(x) for x in ccc[1:-1].split(',')]

print(intersect_check(a, b, c))

