# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

First_name=(input("Enter your first name "))
Last_name=(input("Enter your last name "))
print(''.join(reversed(First_name)) +' '+''.join(reversed(Last_name)) )