alpha = 'abcedefghijklmnopqrstuvxyz'
numeric = []
for char in alpha: 
    number = ord(char) - 97
    numeric.append(number)
print(numeric)