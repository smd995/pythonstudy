A, B = map(int,input().split())
-10000 <= A, B <= 10000
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")