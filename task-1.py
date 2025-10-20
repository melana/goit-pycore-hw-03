from datetime import datetime

def get_days_from_today(date):
    try:
        today = datetime.today().date() # поточна дата
        check_date = datetime.strptime(date, "%Y-%m-%d").date() # задана дата, перетворена в об'єкт date необхідного формату
      
        days_from_today = (today - check_date).days 
        
        return days_from_today
    
    except ValueError:
        # якщо дата введена в неправильному форматі
        return ("Перевірте, чи правильно введено дату. Необхідний формат: РРРР-ММ-ДД")

#Tests
print (get_days_from_today("2002-09-12"))
print (get_days_from_today("2047-06-07"))
print (get_days_from_today("2015-59-47"))
print (get_days_from_today("16-04-1984"))
print (get_days_from_today("17 травня 1934"))