def solve(a):
    ans = 0
    for i in range(0, a + 1):
        ans += i
    return ans

num = int(input())

a = solve(num)

print(a)