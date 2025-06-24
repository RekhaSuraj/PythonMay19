# Write a program to calculate percentage of marks taking inputs from user
# There are 5 subjects

sub1 = int(input('Enter subject1 marks'))
sub2 = int(input('Enter subject2 marks'))
sub3 = int(input('Enter subject3 marks'))
sub4 = int(input('Enter subject4 marks'))
sub5 = int(input('Enter subject5 marks'))

percen_marks = (sub1+sub2+sub3+sub4+sub5)*100/500

print(f'percentage is {percen_marks}%')

# Enter subject1 marks95
# Enter subject2 marks98
# Enter subject3 marks99
# Enter subject4 marks100
# Enter subject5 marks97
# percentage is 97.8%