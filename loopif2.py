n=input("enter the number: ")
n=int(n)
result=0
for num in range(n):
    if num%4==0:
        print(num)
        result+=num

print(result)        