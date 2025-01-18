from cryptography.fernet import Fernet

# def key_gen():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def key_load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?")
key = key_load() + master_pwd.bytes
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(":")
            print("User:", user, ", Password:", passw)
    

def add():
    name = input('Account Name: ')
    pwd  = input('Password: ')
    
    with open('password.txt', 'a') as f:
        f.write(name + ' : ' + pwd + '\n')
        print('[+] Password saved.')



while True:
    mode = input("Woould you like to add a new password or view existing ones(view, add)? Press q to quit.   ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue