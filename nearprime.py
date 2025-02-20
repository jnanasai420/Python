# 1) WAP to print the nearest prime to the given number
# input: Enter number: 18
# output: 17 19
# input: Enter number: 25
# output: 23



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



# WAP to print the sum of max and min prime in a given number
# input: Enter number: 1875
# output: 12


num = input("Enter a number: ")
prime_digits = []

for d in num:
    d = int(d)
    if d > 1:
        is_prime = True
        for i in range(2, int(d ** 0.5) + 1):
            if d % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_digits.append(d)

if prime_digits:
    print(max(prime_digits) + min(prime_digits))
else:
    print("No prime digits found.")









