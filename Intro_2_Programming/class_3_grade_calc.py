
## Grade Calculator ##
## write a program that calculates the grade of an assignment using
## the following guidelines:
## 90-100:A
## 80-89:B
## 70-79:C
## 60-69:D
## Less than 60: F

grade = int(input('What is the student\'s grade?\n'))

if grade < 0 | grade > 100:
    print('That is not a valid score')
elif grade <= 100 & grade >= 90:
    print('A')
elif grade <= 89 & grade >= 80:
    print('B')
elif grade <= 79 & grade >= 70:
    print('C')
elif grade <= 69 & grade >= 60:
    print('D')
elif grade < 60:
    print('F')
else:
    print('Sorry, we only accept integer grades.')
