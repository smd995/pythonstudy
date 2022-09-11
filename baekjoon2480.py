a, b, c = map(int,input().split())
if a == b == c:
    print(10000+a*1000)
else:
    if a == b != c:
        print(1000+a*100)
    else:
        if a == c != b:
            print(1000+a*100)
        else:
            if b == c != a:
                print(1000+b*100)
            else:
                if a > b > c or a > c > b:
                    print(a*100)
                else:
                    if b > a > c or b > c > a:
                        print(b*100)
                    else:
                        if c > a > b or c > b > a:
                            print(c*100)
                        else:
                            pass
