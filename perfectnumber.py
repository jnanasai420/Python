# program to check the given number is perfect number or not 
# perfect no= sum of its divisors except itself must me equal to that number 
# then that number  will be a perfect number


# num=int(input("enter a number:"))
# sum=0
# for i in range(1,(num//2)+1):
#   if num%i==0:
#     sum+=i
# if sum==num:
#   print(f"{num} is perfect number")
# else:
#   print(f"{num} is not a perfect number")


# To print the perfect numbers b/w two numbers
# num=int(input("enter a number:"))
# for j in range(1,num+1):
#   sum=0
#   for i in range(1,(j//2)+1):
#     if j%i==0:
#       sum+=i
#   if sum==j:
#     print(j)


# print the count of perfect numbers b/w two numbers
num=int(input("enter a number:"))
count=0
for j in range(1,num+1):
  sum=0
  for i in range(1,(j//2)+1):
    if j%i==0:
      sum+=i
  if sum==j:
    count=count+1
print(f"There are {count} perfect numbers between {1} and {num}")




  

  
