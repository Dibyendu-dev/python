score=79
if score>101:
    print("pls enter your valid score")
    exit()

if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>70:
    grade="c"
elif score>=60:
    grade="D"
else:
    grade='F'

print("Your Grade is",grade)
