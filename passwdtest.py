from passlib.hash import pbkdf2_sha256

def get_passwd_hash():
    try:
        with open ("userpasswd", "r") as myfile:
            return myfile.read()
    except:
        # Generate default password "password"
        hash = '$pbkdf2-sha256$29000$dc45J4SQ0lrr/b/XGmNMaQ$VDmYehyEzfaDpx0iN4uQShQqgTl.dd/oCiFqR3hpUUE'
        set_passwd_hash(hash)
        return hash

def set_passwd_hash(new_hash):
    with open ("userpasswd", "w") as myfile:
        return myfile.write(new_hash)

def update_passwd():
    new_passwd = input("Enter new password: ")
    hash = pbkdf2_sha256.hash(new_passwd)
    set_passwd_hash(hash)

def check_login_user(username,password):
    passwd_hash = get_passwd_hash()
    try:
        assert username == "user"
        try:
            assert pbkdf2_sha256.verify(password, passwd_hash)
            print("Login successful.")
            return True
        except:
            print("Wrong Password.")
            return False
    except:
        print("Unknown user.")
        return False

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    login_success = check_login_user(username,password)
    if login_success != True:
        exit()
    print("What would you like to do?")
    print("1. Update password.")
    print("2. Exit")
    choice = int(input("Choice: "))
    if choice == 2:
        exit()
    if choice == 1:
        update_passwd()
    
