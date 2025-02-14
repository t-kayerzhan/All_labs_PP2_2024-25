def squares(a, b):
    for num in range(a, b + 1):
        print(num ** 2)  


a, b = map(int, input().split())


squares(a, b)
