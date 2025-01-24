import random
import string

# Function to generate a strong password
def generate_password(length):
    # Define the character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password from the character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Function to get user input and generate the password
def main():
    print("Welcome to the Password Generator!")
    
    # Get desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length < 8:
                print("Password length should be at least 8 characters for better security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
