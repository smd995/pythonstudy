Test_Score = int(input())
if Test_Score <= 100 and Test_Score >= 90:
    print("A")
elif Test_Score <= 89 and Test_Score >= 80:
    print("B")
elif Test_Score <= 79 and Test_Score >= 70:
    print("C")
elif Test_Score <= 69 and Test_Score >= 60:
    print("D")
else:
    print("F")