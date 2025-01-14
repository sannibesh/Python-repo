import math
while True:
    n = input("Please enter a positive number (0 to exit): ")
    n = int(n)
    if n < 0:
        print("Only positive numbers. Please try again.")
        continue
    if n == 0:
        break
    print("square root of", n, "is", sqrt.math(n))