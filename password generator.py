import random

def generate_password(length=8):
    all_characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+[]{}|\:;"<>,.?/')
    random.shuffle(all_characters)
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Generate 10 passwords of length 10
passwords = []
for _ in range(10):
    passwords.append(generate_password(10))

print(passwords)
