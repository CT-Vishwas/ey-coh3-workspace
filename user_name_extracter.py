# Given an Email ID, Extract the user name
# Eg. 
# input: vishwas@cloudthat.com
# output: username is vishwas
email = input("Enter Email Address: ")
if(email.find("@") != -1 and email.count('@') <= 1 and len(email[:email.find("@")]) >= 3):
    print(f"The username is {email[:email.find("@")]}") 
else:
    print(f"{email} is INVALID")