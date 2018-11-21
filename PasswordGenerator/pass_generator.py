import string
import secrets
import pyperclip

# Sets character sets
specials = list(string.punctuation)
chars = list(string.ascii_lowercase)

# Gets password length from user
print("Please enter password length")
length = int(input())

# Add all the character sets together and build password by choosing random options
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for i in range(length))

# Copy to clipboard
pyperclip.copy(password)
print("Done. Password copied to clipboard.")
input()
