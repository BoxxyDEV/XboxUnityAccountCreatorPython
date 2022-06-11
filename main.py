# This script was made by boxuga and xbox unity no hate to you your account creation method is very insecure
from ast import Break
from operator import indexOf
from urllib import request
import requests

usrname = input("Please enter your Username: ")
ValidateUSRTaken = requests.get("http://xboxunity.net/Resources/Lib/ValidateUser.php?uname=" + usrname)
if ValidateUSRTaken.text == '{"Result":false}':
    print("Username Taken")
    exit()
fullname = input("Please enter your name: ")
email = input("Enter your email: ")
ValidateEmail = requests.get("http://xboxunity.net/Resources/Lib/ValidateEmail.php?email=" + email)
if ValidateEmail.text == '{"Result":false}':
    print("An account already exists with that email ")
    exit()
password = input("Please enter your password:  ")
sendUserData = requests.get("http://xboxunity.net/Resources/Lib/Register.php?username=" + usrname + "&email=" + email + "&fullname=" + fullname + "&password=" + password)

if sendUserData.text == '{"Error":"","Success":"Added User"}':
    print('User Created Successfully.')
else:
    print('Something went wrong')

viewrawdata = input('Would you like to view the raw data [y/n]? ')

if viewrawdata == 'n':
    exit()


print(sendUserData.status_code)
print(sendUserData.text)
