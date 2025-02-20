# wap to print given no fibonocii numbers ie., 3 =>4,6,7
# write a program to print given no of nonfibonocii numbers 
# 0 1 1 2 3 5 8 13 21 34 55.... is the fibonocii series 
# but we want non fibonocii number so that we want to print the numbers bw these fibinocii numbers
num=int(input("Enter a number:"))
a,b,nonfib=0,1,0
sum=0
while (nonfib!=num):
    for i in range(a+1,b):
       nonfib+=1
       print(i,end=" ")
       sum=sum+i
       if nonfib==num:
          break
    a,b=b,a+b
print(sum)