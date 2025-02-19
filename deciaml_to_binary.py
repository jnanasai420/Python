# 1) WAP to convert the decimal to binary
# input: Enter a number: 5
# output: 101



# 

num=int(input("Enter a number:"))
s=""
while num!=0:
  res=num%2
  s=str(res)+s
  num=num//2
print(s)


