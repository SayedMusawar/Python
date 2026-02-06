testScore = float(input("Enter your test score"))

if testScore >= 0 and testScore <= 100:
    if testScore in range(90,101):
        print("A")
    elif testScore in range(80,90):
        print("B")
    elif testScore in range(70,80):
        print("C")
    elif testScore in range(60,70):
        print("D")
    elif testScore < 60:
        print("F")
elif testScore < 0:
    print("Marks cannot be less than 0")
else:
    print("Marks cannot be more than 100")