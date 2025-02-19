num=int(input("Enter a number:"))
def isprime(n):
  if n>1:
    for i in range(2,(n//2)+1):
      if n%i==0:
        return False
      return True
  return False
if(isprime(num)):
  print("The number is prime")
else:
  lp,rp=num-1,num+1
  while True:
    if isprime(lp):
      print(f"Nearest prime number on left side is :{lp}")
      break
    lp-=1
  while True:
    if isprime(rp):
      print(f"Nearest prime number on right side is :{rp}")
      break
    rp+=1