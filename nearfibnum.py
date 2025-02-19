num=int(input("enter a number:"))
a,b=0,1
i=1
while (a<=num):
  c=a+b
  a=b
  b=c
print(b-a,a)
res=b-a if (num-(b-a)<a-num) else a;
print(res)