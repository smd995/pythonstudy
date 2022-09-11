Yoon_Nyeon = int(input())
if Yoon_Nyeon % 4 == 0 and Yoon_Nyeon %100 != 0 or Yoon_Nyeon % 400 == 0:
    print(1)
else:
    print(0)