num=input("Enter a number:")
fibsum=0
def is_fib(n):
  a,b=0,1
  while True:
    if a==n:
      return True
    if a>n:
      return False
    a,b=b,a+b
for i in num:
  if(is_fib(int(i))):
    fibsum+=int(i)
print(fibsum)




