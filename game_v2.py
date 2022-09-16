"""Game Guess the Number"""
"""Comp is choosing and guessing the number itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Guessing the number in random

    Args:
        number (int, optional): the choosing number. Defaults to 1.

    Returns:
        int: the count of attempts
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # the guessiing number
        if number == predict_number:
            break #exit from cycle if the number was guessed
    return(count) 

def score_game(random_predict) -> int:
    """how many is guessing right in average by 1000 attempts

    Args:
        random_predict (_type_): the guessing funcion

    Returns:
        int: average quantity
    """
    count_ls = [] 
    np.random.seed(1) #stand the 'seed' in for prodation
    random_array = np.random.randint(1, 101, size=(1000)) #get a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
        
    score = int(np.mean(count_ls))
    print(f'Your program guesses the number in average by {score} attempts')
    return(score) 

#RUN
if __name__ == '__main__':
    score_game(random_predict)