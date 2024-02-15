
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid numbers.")
            return
        
        for i in range(num_passwords):
            password = generate_password(password_length)
            print(f"Password {i+1}: {password}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()