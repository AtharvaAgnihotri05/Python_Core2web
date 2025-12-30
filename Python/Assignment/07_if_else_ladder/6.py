
char = input("Enter char :")

if ord(char) >= 65 and ord(char) < 91:
    print("Uppercase")
elif ord(char) >= 97 and ord(char) < 123:
    print("Lowercase")
elif ord(char) >= 30 and ord(char) < 40:
    print("Numeric")
else:
    print("Special Char")

