
ourstr = input("Enter something: ")

lowcase = 0
upcase = 0

for sym in ourstr:
    if sym.islower():
        lowcase += 1
    elif sym.isupper():
        upcase += 1

print("Number of lowercase symbols:", lowcase)
print("Number of uppercase symbols:", upcase)