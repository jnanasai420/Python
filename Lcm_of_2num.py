a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
max1=a if a>b else b
temp=max1
while True:
  if max1%a==0 and max1%b==0:
    print(f"LCM of {a}and{b} is :",max1)
    break
  max1+=temp
  # lcm=a*b//(gcd(a&d))
  # GCD of two numbers when lcm is known
print(f"Gcd of{a}and{b} is :",((a*b)//max1))