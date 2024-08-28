""" Игра угадай число""" 

<<<<<<< HEAD
import numpy as np 
=======
import numpy as np
>>>>>>> 662c033 (Initial commit)

number = np.random.randit(1, 101) #загадаем число

#количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100'))
    
    if predict_number > numder:
        print("Число должно быть меньше!")
        
    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла