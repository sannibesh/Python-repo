n1=float(input('enter 1st number: '))
n2=float(input('enter 2nd number: '))
n3=float(input('enter 3rd number: '))

if n1>n2:
    max=n1
else:
    max=n2

if n3>max:
    max=n3

print(max, 'is the largest number')