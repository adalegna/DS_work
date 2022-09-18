"""Game Guess the Number"""

import numpy as np

number = np.random.randint(1, 101) # choose the number

# the count of attempts
count = 0

while True:
    count+=1
    predict_number = int(input('Guess the Number from 1 to 100')) 
    
    if predict_number > number:
        print('The Number supposed to be smaller')
    elif predict_number < number:
        print('The Number supposed to be bigger')
    
    else:
        print(f'You guess the Number! This number = {number}, in {count} attempts')
        break # end of the game, exit from a cycle