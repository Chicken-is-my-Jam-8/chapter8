
# Alexander J. Jackson
# name_login.py

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
student_id = input("Enter your student ID number: ")

first_slice = first_name[:3]
last_slice = last_name[:3]
id_slice = student_id[-3:]

login_name = first_slice + last_slice + id_slice 

print(f'Your system login name is:\n{login_name}')
