H, M = map(int,(input().split()))
c = 45
if M > c:
    print(H%24, (M-c)%60)
else:
    if M == c:
        print(H%24, 0)
    else:
        print((H-1)%24, (M+15)%60)