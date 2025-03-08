num = int(input("Enter the number of values: "))


mytuple = tuple(input("Enter True/False: ").strip().capitalize() == "True" for _ in range(num))


if all(mytuple):
    print("You are very truthful")
else:
    print("Lie Lie Lie")
