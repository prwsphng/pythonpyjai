import random

def playing(guess,number):
    if(guess < number):
        return 'too low for this number'
    elif(guess > number):
        return 'too high for this number'
    elif(guess == number):
        return 'you win! congratulations'

def easy():
    for i in range(10):
        temp = int(input('guess the numer between 1-100: '))
        print(playing(temp,num))

        x = 9-i
        print(f"attemp we have left: {x}")

        if(x==0):
            print('you lose')

        if(playing(temp,num) == 'correct'):
            break

def hard():
    for i in range(5):
        temp = int(input('guess the numer between 1-100: '))
        tmp = playing(temp,num)
        print(tmp)

        x = 4-i
        print(f"attemp we have left: {x}")

        if(x==0):
            print('you lose')

        if(tmp == 'correct'):
            break

num = random.randint(1,100)

print(num,'is a number we have to guess')

while input("let's play game (y or n): ").lower() == 'y':
    choice = input('easy or hard: ').lower()

    if(choice == 'easy'):
        easy()

    elif(choice == 'hard'):
        hard()



