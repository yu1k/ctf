# Q6.[Crypto] Classical Cipher
s = input()

for n in s:
    n = ord(n)
    if 97 < n and n < 123: #a ~ z
        n -= 3
    elif 65 < n and n < 91: #A ~ Z
        n -= 3
    c = chr(n)
    print(c, end="")
print("\n")

# cpaw{Caesar_cipher_is_classical_cipher}