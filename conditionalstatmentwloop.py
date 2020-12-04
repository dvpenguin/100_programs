"""#to get each item in list printed i could....

print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4])
print(pets[5], '\n')

#or use a for loop

for doodleledy in pets:
    print(doodleledy)

rock out a conditional statement with a while loop

i_got_20_bucks = 20
while i_got_20_bucks < 35:
    print(i_got_20_bucks)
    i_got_20_bucks += 1
print('I need more money')

never forget the infinite code= meaning it never hits a false
if x = 5
while x >3: make this condistional true for infinite loop
print ('this was a very dumb to run')

for all numbers between 1500 and 2700, wich are divisible by 7 and a multiple of 5

for i in range(1500, 2700):
    if i%7==0 and i%5==0:
        print(i)"""

#write a program that will guess a number between 1 and 10

import random
target_num, guess_num = random.random(1,10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10, and keep guessing till you are right! '))
print('Game over! ')

