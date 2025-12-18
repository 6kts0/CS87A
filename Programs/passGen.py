import random 
import string
import time

# Initialize password 
PASS_DONE = []

# COMPLEXITY OPTION 1 - Letters and numbers only
def pass_letter_num():
    global PASS_DONE
    PASS_DONE = []

    usr_pass_len = input("Enter a preferred length for your password (minimum: 6): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase
    int_pool = string.digits
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
        random_int = random.choice(int_pool)
        PASS_DONE.append(random_int)
    else:
        pass
    password = ''.join(PASS_DONE)
    print(f"Your Password: {password} \n")
    return password


# COMPLEXITY OPTION 2 - Uppercase letters only
def pass_letter_up():
    global PASS_DONE
    PASS_DONE = []

    usr_pass_len = input("Enter a preferred length for your password (minimum: 6): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_upper = string.ascii_uppercase
    while len(PASS_DONE) < usr_pass_len:
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
    else:
        pass
    password = ''.join(PASS_DONE)
    print(f"Your Password: {password} \n")
    return password

# COMPLEXITY OPTION 3 - Lowercase letters only
def pass_letter_low():
    global PASS_DONE
    PASS_DONE = []

    usr_pass_len = input("Enter a preferred length for your password (minimum: 6): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_lower = string.ascii_lowercase
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
    else:
        pass
    password = ''.join(PASS_DONE)
    print(f"Your Password: {password} \n")
    return password

# COMPLEXITY OPTION 4 - Letters and special characters only
def pass_letter_wild():
    global PASS_DONE
    PASS_DONE = []

    usr_pass_len = input("Enter a preferred length for your password (minimum: 6): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase
    char_pool_wild = string. punctuation
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
        random_wild = random.choice(char_pool_wild)
        PASS_DONE.append(random_wild)    
    else:
        pass
    password = ''.join(PASS_DONE)
    print(f"Your Password: {password} \n")
    return password 

# COMPLEXITY OPTION 5 - All available parameters
def pass_gen_all():
    global PASS_DONE
    PASS_DONE = []

    usr_pass_len = input("Enter a preferred length for your password (minimum: 6): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    wild_char = string.punctuation
    int_pool = string.digits
    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)

        random_int = random.choice(int_pool)
        PASS_DONE.append(random_int)

        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)

        random_wild = random.choice(wild_char)
        PASS_DONE.append(random_wild)
    else:
        pass
    password = ''.join(PASS_DONE)
    print(f"Your Password: {password} \n")
    return password


def pass_batch(length, complexity, count):
    passwords = []
    char_pool = ""

    if complexity == 1:
        char_pool = string.ascii_letters + string.digits
    elif complexity == 2:
        char_pool = string.ascii_uppercase
    elif complexity == 3:
        char_pool = string.ascii_lowercase
    elif complexity == 4:
        char_pool = string.ascii_letters + string.punctuation
    elif complexity == 5:
        char_pool = string.ascii_letters + string.digits + string.punctuation
    for i in range(count):
        password = ''.join(random.choice(char_pool) for _ in range(length))
        passwords.append(password)
    return passwords

def batch_pass_gen():
    print('=' * 60)
    print("--- Password Batch Generator ---")
    print('=' * 60)
    try:
        usr_pass_len = int(input("Enter password length (minimum: 6): "))
        if usr_pass_len < 6:
            print("Password length must be at least 6...")
            return
        print('\n')
        print("Complexity Options:")
        print("1 - Letters and numbers")
        print("2 - Uppercase letters only")
        print("3 - Lowercase letters only")
        print("4 - Letters and special characters")
        print("5 - All parameters (most secure)")
        usr_pass_param = int(input("\nEnter complexity (1-5): "))
        if usr_pass_param < 1 or usr_pass_param > 5:
            print("Invalid complexity option!")
            return
        
        pass_count = int(input("Quantity of passwords to generate: "))
        if pass_count == 1:
            print("Must generate at least 1 password...")
            return
        
        print("=" * 60)
        print(f"\nGenerating {pass_count} password(s)...\n")
        passwords = pass_batch(usr_pass_len, usr_pass_param, pass_count)

        for i, pwd in enumerate(passwords, 1):
            print(f"Password {i}: {pwd}")
        print('\n')
        print('=' * 60)
    except ValueError:
        print("\nINVALID INPUT TYPE...")
        time.sleep(0.5)
        print("Please enter valid numbers.\n")

def main():
    print('=' * 60) 
    print("--- Password Generator ---")
    print('=' * 60)
    print("Generate single password - 1")
    print("Generate multiple passwords (batch) - 2")
    print('=' * 60)
    
    try:
        mode = int(input("Enter mode (1 or 2): "))
        
        if mode == 1:
            print('\n' + '=' * 60) 
            print("--- Password Complexity Options ---")
            print('=' * 60)
            print("Only letters and numbers - 1")
            print("Only uppercase letters - 2")
            print("Only lowercase letters - 3")
            print("Only letters and special characters - 4")
            print("Use all available parameters (most complex and secure) - 5")
            print('=' * 60) 
            
            usr_pass_param = input("Enter password complexity parameter (1-5): ")
            usr_pass_param = int(usr_pass_param)
            if usr_pass_param == 1:
                pass_letter_num()
            elif usr_pass_param == 2:
                pass_letter_up()
            elif usr_pass_param == 3:
                pass_letter_low()
            elif usr_pass_param == 4:
                pass_letter_wild()
            elif usr_pass_param == 5:
                pass_gen_all()
            else:
                print('\n')
                print('INVALID PARAMETER OPTION...')
                time.sleep(0.5)
                main()
        
        elif mode == 2:
            batch_pass_gen()
        
        else:
            print('\nINVALID MODE...')
            time.sleep(0.5)
            main()
            
    except ValueError:
        print("\n")
        print("INVALID INPUT TYPE...")
        time.sleep(0.5)
        print("Enter a number 1 or 2 to continue \n")
        time.sleep(0.5)
        main()

if __name__ == '__main__':
    main()