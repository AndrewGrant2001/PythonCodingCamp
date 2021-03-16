# Andrew Grant
# 105226219

number_grade = int(input("Enter your number grade: "))

if 0 <= number_grade <= 49:
    print("Your letter grade is F.")
elif 50 <= number_grade <= 59:
    print("Your letter grade is D.")
elif 60 <= number_grade <= 69:
    print("Your letter grade is C.")
elif 70 <= number_grade <= 79:
    print("Your letter grade is B.")
elif 80 <= number_grade <= 100:
    print("Your letter grade is A.")
else:
    print("Incorrect Input - No information can be given.")