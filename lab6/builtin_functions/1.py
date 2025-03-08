mylist = []

print("Enter 5 numbers:")
for i in range(0, 5):
    num = int(input())
    mylist.append(num)

result = 1;
for num in mylist:
    result *= num

print("Product of these numbers:", result)