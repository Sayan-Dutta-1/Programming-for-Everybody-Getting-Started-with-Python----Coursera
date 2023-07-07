#Question

'''3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.'''

#Answer

score = input("Enter Score between 0.00 to 1.00: ")
scr=float(score)
if scr >= 0.9 and scr <=1.0:
    print("A")
elif scr >= 0.8 and scr < 0.9:
    print("B")
elif scr >= 0.7 and scr < 0.8:
    print("C")
elif scr >= 0.6 and scr < 0.7:
    print("D")
elif scr >= 0.0 and scr <= 0.6:
    print("F")
else:
    print("Error! Enter a number between 0.0 to 1.0")

# Copyright SAYAN DUTTA