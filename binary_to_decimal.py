# write a program to convert the binary number into decimal number ie., 100101 into 37
num=int(input("Enter a number:"))
temp=num
count=dec=0
while num!=0:
    rem=num%10
    dec=dec+(2**count)*rem
    num=num//10
    count+=1
print(f"The Decimal number of {num} is {dec}")