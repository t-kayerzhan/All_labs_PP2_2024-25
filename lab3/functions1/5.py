global res 
res = set({})

def all_permutatons(str, fix = ''):
    if len(str) == 0:
        res.add(fix)
        return 
    
    for i in range(0, len(str)):
        cur = str[i]
        rem = str[:i] + str[i+1:]
        all_permutatons(rem, fix+cur)
        


str = input("Enter the String: ")
print("All permutations of that string: ")
all_permutatons(str)
for x in res:
    print(x)