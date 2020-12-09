import random
import pickle

info = {}

with open("game.p", "br") as readfile:
    info = pickle.load(readfile)
print(info)

s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]{}\|';:<,>.?/`"

len_password = int(input("Write the length password you want: "))

password = "".join(random.sample(s, len_password))
print(password)

answer = input("would you like to keep this password: ")

if "yes" or "y" in answer:
    account_name = input("enter the account name: ")
    website = input("entered the website name: ")
    email = input("enter the email id for the account: ")
    info[account_name] = password, email, website, account_name
    with open("game.p", "bw") as filewrite:
        pickle.dump(info, filewrite, protocol=2)

if "no" or "n" in answer:
    print("ok")
