
# Alexander J. Jackson
# valid_password.py

correct_length = False
has_uppercase = False
has_lowercase = False
has_digit = False

user_password = input("please enter your password: ")

if user_password.isalpha() == True:
    pass
else: has_digit = True

for x in user_password:
    if x.isupper() == True:
        has_uppercase = True
    else:
        pass
    if x.islower() == True:
        has_lowercase = True
    else:
        pass

if has_uppercase == False or has_lowercase == False or has_digit == False:
    print("False")
else:
    print("True")
