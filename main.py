import random


def main():

    l_side = int(input('Enter teh left side: '))
    r_side = int(input('Enter teh right side: '))
    attempts = int(input('Enter attempts count: '))

    if attempts <= 0 or l_side >= r_side:
        print('Input another numbers!!!')
        return


    random_number = random.randint(l_side, r_side+1)
    print(random_number)

    for i in range(1, attempts+1):
        print(f'Its {i} attempts')

        try:
            answer = int(input('Enter your number: '))
        except ValueError:
            print('Input number')
            continue

        if answer == random_number:
            print('You won!!!')
            return

        if answer < random_number:
            print('Too small')
        else:
            print('Too big')

        if i == attempts:
            print('It was your last attempt!!!')
            return
        print('Try again')


if __name__ == '__main__':
    flag = True
    while flag:
        main()
        flag = int(input("Do you want to play again? (1/0)"))
        #print(flag)