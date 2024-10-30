
# Alexander J. Jackson
# valid_password.py

correct_length = False
has_uppercase = False
has_lowercase = False
has_digit = False

user_password = input("please enter your password: ")

if len(user_password) >= 7:
    correct_length = True

for x in user_password:
    if x.isupper() == True:
        has_uppercase = True
    if x.islower() == True:
        has_lowercase = True
    if x.isdigit() == True:
        has_digit = True

if has_uppercase == False or has_lowercase == False :
    print("False")
elif has_digit == False or correct_length == False:
    print("False")
else:
    print("True")
