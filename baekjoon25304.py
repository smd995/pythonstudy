X = int(input())
N = int(input())
s = 0
for i in range(N):
    a, b = map(int, input().split())
    c = a * b
    s += c
if s == X:
    print('Yes')
else:
    print('No')
