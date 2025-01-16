import math

while True:
    n=input("Enter the input: ")
    n=int(n)
    if n < 0:
        print("Error. Please enter a positive number")
        continue
    if n==0:
        break
    print("Square Root of", n, "is", math.sqrt(n))