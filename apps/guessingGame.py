import sys
import random
if len(sys.argv) > 1:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
else:
    start = 1
    end = 10
    pass

print()
print('welcome to the guessing game')
name = input('Your name: ')

lucky_number = random.randint(start, end)

print('Guess the number from the list: ')
print(list(range(start, end+1)))
print()
answer = int(input('Number: '))
print()

count = 3
while answer != lucky_number and count != 0: 
    print(f'The number {answer} is incorrect, you have {count} tries left')
    answer = int(input('Try again: '))
    if answer == lucky_number:  
        break
    else:
        count -=1

if answer == lucky_number:
    print(f'{name} You win the number {answer} is Correct')
else:
    print(f'{name} too many tries you are dead, The correct number was: {lucky_number}')