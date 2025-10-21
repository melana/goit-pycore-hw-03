import re

def normalize_phone(num):
    pattern = r"(?!\+)\D"# видаляє всі символи, крім цифр та символу '+'
    formatted_number = re.sub(pattern,"", num)
    if re.match(r"^380", formatted_number):
        formatted_number = "+" + formatted_number
    elif re.match(r"^80", formatted_number):
        formatted_number = "+3" + formatted_number
    elif re.match(r"^0", formatted_number):
        formatted_number = "+38" + formatted_number

    return formatted_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

