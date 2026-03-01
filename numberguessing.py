#---Number Guessing Game---
import random

def menu():
    while True:
        print("\033[94m---Number Guessing Game---\033[0m")
        print('1 - Normal Game')
        print("\033[32m2 - Custom Game\033[0m")
        print("\033[31m0 - Exit\033[0m")
        choice=int(input(''))
        if choice >= 0 and choice <=2:
            if choice == 1:
                menu2()
            elif choice == 2:
                custommenu()
            elif choice == 0:
                break

def menu2():
    while True:
        print('---Game mode selection:---')
        print("\033[92m1 - Easy (0-10)\033[0m")
        print("\033[93m2 - Medium (0-50)\033[0m")
        print("\033[91m3 - Hard (0-100)\033[0m")
        print('0 - Exit')
        c2=int(input(''))
        if c2 >= 0 and c2 <=3:
            if c2 == 1:
                easy()
            elif c2 == 2:
                medium()
            elif c2 == 3:
                hard()
            elif c2 == 0:
                menu()
            elif c2 == 0:
                menu()

def easy():
    print("\033[92m---Easy (0-10)---\033[0m")
    enumber=random.randint(0,10)
    attempts=0
    while True:
        a=int(input('Guess the number between 1-10:'))
        if a < enumber:
            print("\033[33mThe number is bigger\033[0m")
            attempts+=1
        elif a > enumber:
            print("\033[31mThe number is smaller\033[0m")
            attempts+=1
        elif a == enumber:
            print(f"\033[32mYou guessed the number in {attempts} attempts\033[0m")
            k=input('Would you like to play again? (y/n)')
            if k == 'y':
                menu2()
            elif k == 'n':
                menu()
            while k != 'y' or k != 'n':
                k=input('Would you like to play again? (y/n)')

def medium():
    print("\033[93m---Medium (0-50)---\033[0m")
    mnumber=random.randint(0,50)
    attempts=0
    while True:
        a=int(input('Guess the number between 0-50:'))
        if a < mnumber:
            print("\033[33mThe number is bigger\033[0m")
            attempts+=1
        elif a > mnumber:
            print("\033[31mThe number is smaller\033[0m")
            attempts+=1
        elif a == mnumber:
            print(f"\033[32mYou guessed the number in {attempts} attempts\033[0m")
            k=input('Would you like to play again? (y/n)')
            if k == 'y':
                menu2()
            elif k == 'n':
                menu()
            while k != 'y' and k != 'n':
                k=input('Would you like to play again? (y/n)')

def hard():
    print("\033[91m---Hard (0-100)---\033[0m")
    hnumber=random.randint(0,100)
    attempts=0
    while True:
        a=int(input('Guess the number between 0-100:'))
        if a < hnumber:
            print("\033[33mThe number is bigger\033[0m")
            attempts+=1
        elif a > hnumber:
            print("\033[31mThe number is smaller\033[0m")
            attempts+=1
        elif a == hnumber:
            print(f"\033[32mYou guessed the number in {attempts} attempts\033[0m")
            k=input('Would you like to play again? (y/n)')
            if k == 'y':
                menu2()
            elif k == 'n':
                menu()
            while k != 'y' and k != 'n':
                k=input('Would you like to play again? (y/n)')

def custommenu():
    print("\033[32m---Custom Game---\033[0m")
    x=int(input('What should be the lower limit:'))
    y=int(input('What should be the upper limit:'))
    lives=int(input('How many attempts should you have:'))
    cnumber=random.randint(x,y)
    attempts=lives
    trys=0
    while True:
        if attempts == 0:
            print('You Lose')
            menu()
        a=int(input(f'Guess the number between {x}-{y}: (You have: {attempts} lives)'))
        if a < cnumber:
            print("\033[33mThe number is bigger\033[0m")
            attempts-=1
            trys+=1
            print(f'You have {attempts} lives')
        elif a > cnumber:
            print("\033[31mThe number is smaller\033[0m")
            attempts-=1
            trys+=1
            print(f'You have {attempts} lives')
        elif a == cnumber:
            print(f"\033[32mYou guessed the number in {trys} attempts\033[0m")
            k=input('Would you like to play again? (y/n)')
            if k == 'y':
                custommenu()
            elif k == 'n':
                menu()
            while k != 'y' and k != 'n':
                k=input('Would you like to play again? (y/n)')

menu()