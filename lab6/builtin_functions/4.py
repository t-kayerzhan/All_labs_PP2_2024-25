import math
import time

num = int(input("Enter a number: "))
millisec = int(input("Enter milliseconds to wait: "))
time.sleep(millisec/1000)

print("Square root of", num, "after", millisec, " miliseconds is ", math.sqrt(num))