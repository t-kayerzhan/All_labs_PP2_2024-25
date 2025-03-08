mylist = []

ourstr = input("Enter a string: ")
for letter in ourstr:
    mylist.append(letter.lower())

reversedlist = list(reversed(mylist))

if mylist == reversedlist:
    print("It is a palindrome")
else:
    print("It is not a palindrome")