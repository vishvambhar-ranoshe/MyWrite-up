import string

with open("message.txt") as filep:
    cipher = filep.read()
    print(cipher)
    num = [int(val) for val in cipher.split()]
    for num in num:
        mod = num % 37

        if mod in range(26):
            print(string.ascii_uppercase[mod], end="")
        elif mod in range(26, 36):
            print(string.digits[mod - 26], end="")
        else:
            print("_", end="")

