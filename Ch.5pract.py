#Write a program that accepts a student’s full name and their final grade average (i.e. 95). Then using an IF ELIF ELSE statement,
#  display the letter grade using the following legend:

#Author: Brent J. Smith

sFullName = input("Enter the student's full name.")

iFinalAve = int(input("Enter the student's final grade average."))

if (iFinalAve >= 94):
    sLetterGrade = 'A'
elif (iFinalAve >= 90):
    sLetterGrade = 'A-'
elif (iFinalAve >= 87):
    sLetterGrade = 'B+'
elif (iFinalAve >= 83):
    sLetterGrade = 'B'
elif (iFinalAve >= 80):
    sLetterGrade = 'B-'
else :
    sLetterGrade = 'C'

print(sFullName + " had a final average of " + str(iFinalAve) + " which resulted in a(n) " + sLetterGrade + " for the course.")

     