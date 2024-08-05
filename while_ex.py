secret_uname,  secret_pwd = 'admin', 'admin'

while True :
    print("welcome to admin login")
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == secret_uname and password == secret_pwd :
           print('login successful')

    break
else:
            print('Invalid credentials')
            print("please try again!")

