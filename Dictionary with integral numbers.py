"""Given integral numbern, create a dictionary with the key value function that creates the
integral is a number assinged to a function"""
print('Enter in a number: ')
n= int(input())
d= dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)