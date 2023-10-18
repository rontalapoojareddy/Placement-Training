'''c=int(input())
a=bin(c)[2:]
count=0
for i in a:
    if i=='1':
        count=count+1
print(count)'''
"""def isPowerOfTwo(num):
    if num <= 0:
        return False  # Non-positive numbers are not powers of 2.
    return (num & (num - 1)) == 0

# Test the function
num = int(input("Enter a number: "))
if isPowerOfTwo(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is not a power of 2.")
"""
'''import math

def isPowerOfFour(num):
    if num <= 0:
        return False  # Non-positive numbers are not powers of 4.

    log_value = math.log(num, 4)
    return log_value.is_integer()

# Test the function
num = int(input("Enter a number: "))
if isPowerOfFour(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is not a power of 4.")'''
''' power of 4
def isPowerOfTwo(num):
    if num <= 0:
        return False  # Non-positive numbers are not powers of 2.
    return (num & (num - 3)) == 0

# Test the function
num = int(input("Enter a number: "))
if isPowerOfTwo(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is not a power of 4.")'''
'''
MISSING NO
def find_missing_number(arr):
    n = len(arr) + 1  # Calculate the expected length of the array
    expected_sum = (n * (n + 1)) // 2  # Calculate the expected sum of consecutive integers
    
    actual_sum = sum(arr)  # Calculate the actual sum of the elements in the array
    
    missing_number = expected_sum - actual_sum  # The difference is the missing number
    
    return missing_number

# Example usage:
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print(f"The missing number is: {missing_number}")'''
'''def find_lonely_number(arr):
    lonely_number = 0
    
    for num in arr:
        lonely_number ^= num
    
    return lonely_number

# Example usage:
arr = [1, 2, 3, 4, 3, 2, 1]
lonely_number = find_lonely_number(arr)
print(f"The lonely number is: {lonely_number}")'''
'''import math
'''
factorial_100000 = math.factorial(100000)
print(factorial_100000)'''
def toh(n,source,auxilary,destination):
    if n==0:
        return
    toh(n-1,source,destination,auxilary)
    print("disk",n,"moved from",source,"to",dest)
    toh(n-1,aux,source,dest)
n=int(input())
source,aux,dest=input().split()
toh(n,source,aux,dest)
o/p:
    3
a b c
disk 1 moved from a to c
disk 2 moved from a to c
disk 1 moved from b to c
disk 3 moved from a to c
disk 1 moved from b to c
disk 2 moved from b to c
disk 1 moved from b to c'''