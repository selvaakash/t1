num = int(input("Enter the value of n: "))
a=0
b=1
if num>1:
    for x in range(num):
        a=a+b
        b=b+1
    print(a)
else:
    print("Invalid")
