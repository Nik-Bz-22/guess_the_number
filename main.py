import random


def main():
    flag = True

    l_side = int(input('Enter teh left side: '))
    r_side = int(input('Enter teh right side: '))
    attempts = int(input('Enter attempts count: '))

    if attempts <= 0:
        print('Input another attempts count!!!')
        return

    if l_side >= r_side:
        print('Input another numbers!!!')
        return

    random_number = random.randint(l_side, r_side+1)
    print(random_number)

    for i in range(1, attempts+1):
        print(f'Its {i} attempts')
        try:
            answer = int(input('Enter your number: '))
        except TypeError:
            print('Input number')
            continue

        if answer == random_number:
            print('You won!!!')
            return

        else:
            if i == attempts:
                print('It was your last attempt!!!')
                return
            print('Try again')


if __name__ == '__main__':
    main()