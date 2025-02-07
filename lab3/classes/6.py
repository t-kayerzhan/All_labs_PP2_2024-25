def isXprime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

listIn = list(input("Enter numbers separated by spaces: ").split())

prime_numbers = list(filter(lambda x: isXprime(x), listIn))

print("Prime numbers list: ")
for x in prime_numbers: 
    print(x)