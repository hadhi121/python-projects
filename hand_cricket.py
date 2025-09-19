import random 
name  = input('type your name: ')
print('Welcome ',name,'to this HAND CRICKET GAME')


comp_pick = ''
options = ['bowl' , 'bat']
#toss
print('\n----TOSS TIME------\n')
user_pick = input('choose odd or even: ').strip().lower()
if user_pick == 'odd':
    comp_pick = 'even'
else:
    comp_pick = 'odd'

print(f'\nYou choose {user_pick} and computer choose {comp_pick}.')

user_num = int(input('\nchoose a number b/w 1 to 6: '))
comp_num = random.randint(1,6)
print(f'\ncomputer picked : {comp_num}')

total = user_num + comp_num
if (total % 2 == 0 and user_pick == 'even') or (total % 2 == 1 and user_pick == 'odd'):
    print('\nuser won the toss')
    user_decision = input('\ndo you want to Bat or Bowl first? ' ).strip().lower()
    if user_decision == 'bat':
        comp_decision = 'bowl'
    else:
        comp_decision = 'bat'

else:
    print('\nComputer won the toss ')
    comp_decision = random.choice(options)
    if comp_decision == 'bat':
        user_decision = 'bowl'
    else:
        user_decision = 'bat'

    print(f'Computer chooses to {comp_decision} first.')

user_score = 0
comp_score = 0

if user_decision == 'bat' or comp_decision == 'bowl':
    
    while True:
        print("\n--- USER BATTING ---")
        user = int(input('enter your run(1-6): '))
        computer = random.randint(1,6)
        print(f'computer picked',computer)
        
        if user == computer:
            print('\n-----USER IS OUT------\n')
            break
        else:
            user_score += user
            print(f'\nuser score is',user_score)

    print(f'\nTotal score of user is',user_score)

    print("\n--- COMPUTER BATTING ---")
    while True:
        user = int(input('\nenter your Bowl(1-6): '))
        computer = random.randint(1,6)
        print(f'\ncomputer picked',computer)
        
        if user == computer:
            print('\n-----COMPUTER IS OUT------\n')
            break
        else:
            comp_score += computer
            print(f'\ncomputer score is',comp_score)
            if comp_score > user_score:
                break
    print(f'\nTotal score of computer is',comp_score)

elif user_decision == 'bowl' or comp_decision == 'bat' :
    print("\n--- COMPUTER BATTING ---")
    while True:
        user = int(input('\nenter your Bowl(1-6): '))
        computer = random.randint(1,6)
        print(f'\ncomputer picked',computer)
        
        if user == computer:
            print('\n-----COMPUTER IS OUT------\n')
            break
        else:
            comp_score += computer
            print(f'\ncomputer score is',comp_score)

    print(f'\nTotal score of computer is',comp_score)

    print("\n--- USER BATTING ---")
    while True:
        user = int(input('\nenter your run(1-6): '))
        computer = random.randint(1,6)
        print(f'\ncomputer picked',computer)
        
        if user == computer:
            print('\n-----USER IS OUT------\n')
            break
        else:
            user_score += user
            print(f'\nuser score is',user_score)
            if user_score > comp_score:
                break
    print(f'\nTotal score of user is',user_score)


print("\n🏆 Match Over! 🏆")
if user_score > comp_score:
    print("\nUser Win! 🎉")
elif user_score < comp_score:
    print("\nComputer Wins! 🤖")
else:
    print("\nIt's a Tie! 🤝")

            
