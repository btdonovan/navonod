#! /usr/bin/python

# per the input definition, the first line is the number of lines that will follow.
t = int(input())

# We accept t more lines of input and add those lines to a list nums
nums = []
while t:
    t -= 1
    nums.append(int(input()))

def z(num):
    ''' The function z accepts a single positive integer num as its argument. The output of z will be equal to the number of trailing zeros in the factorial of num.'''
    count = 0                   # initialize our count for num
    v = 5                  # Set an initial value for v. V will represent successive exponents of 5.
    while num >= v:             # We don't want exponents of five that are larger than num.
        count += num // v   # count will equal count + num / v while v <= num
        v = v * 5          # Eventually this will set v to a value greater than num and the loop will end.
    return count

# apply function z to items in nums and print result
for i in nums:
    print(z(i))

