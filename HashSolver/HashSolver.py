import hashlib
to_crack = input("Please input SHA-1 hash to crack:\n")

with open("top1000000passwords.txt", "r") as data:
    for guess in data:
        hashed_guess = hashlib.sha1(bytes(str(guess.replace('\n', '')), 'utf-8')).hexdigest()

        if hashed_guess == to_crack:
            print("The password is "+str(guess))
            quit()
