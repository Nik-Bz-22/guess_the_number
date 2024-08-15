import random

flag = True


l_side = int(input('Enter teh left side: '))
r_side = int(input('Enter teh right side: '))


if l_side >= r_side:
    print('Input another numbers!!!')
    flag = False

random_number = random.randint(l_side, r_side+1)
print(random_number)

while flag:
    answer = int(input('Enter your number: '))
    if answer == random_number:
        print('You won!!!')
        flag = False

    else:
        print('Try again')
