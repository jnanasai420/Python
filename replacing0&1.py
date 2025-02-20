# 1) Problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones and all the ones with zeroes.

# Examples:

# Example 1:
# Input: N = 502113
# Output: 512003


n = input()  
num_str = str(n)
new_num_str = ""

for digit in num_str:
    if digit == '0':
        new_num_str += '1'
    elif digit == '1':
        new_num_str += '0'
    else:
        new_num_str += digit  

result = int(new_num_str)
print(result)




# 2) Problem Statement: Check if the number is a Harshad(or Niven) number or not.

# Examples:

# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

# Example 2:
# Input: 379
# Output: No
#  it is not a Harshad number.
# Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.

num=int(input("Enter a number:"))
sum=0
for i in str(num):
    sum+=int(i)
print("harshad number") if num%sum==0 else print(" Not aharshad number")
    

