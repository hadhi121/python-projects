import random 
import time

OPERATORS = ['+','-','*']
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 5

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr , answer

input('PLEASE PRESS ENTER TO PLAY!!! ')
print('-----------------------------')

wrong = 0
start_time = time.time()
score = 0
for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        user_guess = input('Problem #'+ str(i+1) + ': ' + expr + ' = ')
        if user_guess == str(answer):
            score+=1
            break
        else:
            wrong += 1

end_time = time.time()
total_time = end_time - start_time

print('----------------------------')    
print(f'YOU GOT {str(score)}/{TOTAL_PROBLEMS} IN THIS MATH TEST.')
print('Great job! You finished in ',round( total_time, 2 ) , 'seconds.')

    

