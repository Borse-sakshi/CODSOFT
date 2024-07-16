import random
import string

def generate_password(length, complexity):
    """Generate a random password based on given length and complexity"""
    if complexity == 'weak':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase 
    else:
        raise ValueError("Complexity should be one of: 'weak', 'medium', 'strong'")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator App")

    print("------------------------------------")
    
    length = int(input("Enter the length of the password: "))

    print("------------------------------------")
    
    complexity = input("Enter the complexity (weak/medium/strong): ").lower()
    
    try:
        password = generate_password(length, complexity)
        print("====================================")
        print(f"\nGenerated Password: {password}")
        print("==========XXX==========")
    except ValueError as ve:
        print(f"Comlexity not found: {ve}")

if __name__ == "__main__":
    main()
