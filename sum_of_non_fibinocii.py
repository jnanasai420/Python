# 2) WAP to print the sum of non-fib numbers as per the input
# input: Enter no. of non-fib series: 3
# output: 17
num=int(input("enter a number :"))
a,b,nonfib=0,1,0
sum=0
while nonfib!=num:
    for i in range(a+1,b):
        nonfib+=1
        # print(i,end=" ")
        sum=sum+i
        if (nonfib==num):
           break
    a,b=b,a+b

print(f"The sum of first {num} non-Fibonacci numbers is {sum} ")


