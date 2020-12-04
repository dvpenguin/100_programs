""" computer the factorial of a given number, result printed in csv single line
factorial is the integer product of a number and all numbers below it
4! is 4*3*2*1=24"""

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
print('Enter an integer... ')
num = int(input())
print(factorial(num))
