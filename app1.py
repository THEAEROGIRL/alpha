
def register():
    names=[]
    usernames=[]
    passwords=[]
    names.append(input("name:"))
    usernames.append(input("username:"))
    passwords.append(input("password:"))
    return usernames
def login(username,password):
    usernames=[]
    passwords=[]
    password=""
    username=""
    username=input("username:")
    password=input("password:")
    if password==passwords[username.index(username)]:
        print("login successful")
    else:
        print("incorrect")
account_ans=""
while True:
    account_ans=input("login or register:")
    if account_ans=="register":
        register()
    elif account_ans=="login":
        password=""
        username=""
        usernames=[]
        passwords=[]
        login(usernames,passwords)
    else:
        break