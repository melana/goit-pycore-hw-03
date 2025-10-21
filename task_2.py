import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min >= 1 & max <=1000 & quantity < max: #перевірка, що вхідні параметри відповідають заданим обмеженням
            res = set() # викорисвуємо множину, щоб забезпечити унікальні числа
            for i in range(quantity):
                num = random.randint(min, max) # генерація рандомних чисел в заданому діапазоні
                res.add(num)
            return sorted(res)
    finally:
        # якщо що вхідні параметри не відповідають заданим обмеженням
        return ("Перевірте правильність параметрів: min - не менше 1, max - не більше 1000")
    
print (get_numbers_ticket(1,100,5)) 
