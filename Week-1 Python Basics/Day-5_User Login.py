def register_user():
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")
    print("Registration successful.")

def login_user():
    username = input("Username: ")
    password = input("Password: ")
    for line in open("users.txt", "r"):
        saved_user, saved_pass = line.strip().split(":", 1)
        if username == saved_user and password == saved_pass:
            print("Login successful.")
            return
    print("Login failed. Invalid credentials.")

if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")
            