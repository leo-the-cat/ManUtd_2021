"""This function gueses randomly chosen number.
     It returns a total amount of attempts"""

def guess_number(number):
    
    global left
    global right
    predict = random.randint(left,right)
    count = 1
    while number != predict:   
        a = (left + right) // 2      
            # a is an auxiliary variable
        count+=1
        predict = random.randint(left,right)
        if a > number:
            right = a
        elif a < number:
            left = a
    return(count)
    
"""This programm uses guess_number(number) """

import random
left=1
right=1000
number = random.randint(left,right)
print ("Загадано число от 1 до 1000")
result = guess_number(number)
print('Загаданное число',number)
print('Угадано с',result,'попыток')