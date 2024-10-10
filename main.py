#importing important libraries
import random
import time

#declaring variables which will be used
number = int(input('Choose a number:\n'))
result = 0

#sarting timer
start = time.time()

#creating a loop for giving multiplication answers
for i in range (0,10):
    r = random.randint(1, number)
    print(number,'*',r,'=')
    answer = int(input())
    if answer == number * r:
        result +=1
    else:
        continue

#ending timer
end = time.time()

#obtaining results
if result == 10:
    print('Excellent!')
elif result == 9:
    print('Very good.')
elif result == 7 or result == 8:
    print('Good.')
elif result == 4 or result == 5 or result == 6:
    print('Average.')
elif result == 3 or result == 2 or result == 1:
    print('You should rework this table.')
else:
    print('You MUST rework this table.')

#time for doing the task
print('Doing this task took', int(end-start), 'seconds for you.')