from datetime import datetime,timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()# сьогоднішня дата (на момент здачі 20.10.25)
    upcoming_birthdays = []
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")#
        birthday_this_year = user_birthday.replace(year = today.year).date()
        if birthday_this_year < today:# перевіряємо, чи вже минув день народження в цьому році
            continue
        elif (birthday_this_year - today).days <=6:
            if birthday_this_year.weekday() == 5:# якщо день народження в суботу
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:# кщо день народження в неділю
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({"name": (user["name"]), "congratulation_date": datetime.strftime(congratulation_date, "%Y.%m.%d")})
    return upcoming_birthdays




users = [
    {"name": "John Doe", "birthday": "1985.10.26"}, # в межах 7 днів, неділя 
    {"name": "Jane Smith", "birthday": "1990.10.24"},# в межах 7 днів 
    {"name": "Ann Miller", "birthday": "1990.11.20"},# не в межах 7 днів
    {"name": "Sam Roberts", "birthday": "1995.03.21"}# не в межах 7 днів
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)