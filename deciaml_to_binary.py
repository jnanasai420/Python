# 1) WAP to convert the decimal to binary
# input: Enter a number: 5
# output: 101



num=int(input("Enter a number:"))
s=""
while num!=0:
  res=num%2
  s=str(res)+s
  num=num//2
print(s)




# 2) WAP to print the sum of non-fib numbers as per the input
# input: Enter no. of non-fib series: 3
# output: 17



num=int(input("Enter a number:"))
a,b,nonfib=0,1,0

while (nonfib!=num):
    for i in range(a+1,b):
       nonfib+=1
       print(i,end=" ")
       
       if nonfib==num:
          break
    a,b=b,a+b


