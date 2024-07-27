import random, string

# Task 1
# Напишіть функцію, яка приймає суму доходу користувача і податкову ставку у відсотках,
# а повертає розраховану суму податку, яку потрібно сплатити.
# def money(x=0, y=0):
#     x = int(input("сума ? >>> "))
#     y = int(input("процент податку ? >>> "))
#     return (x / 100) * y
#
# print("сплата податку у розмірі: ", money())

# -------- варіант_2 --------
# suma = 1000
# podatok = 15
# def money(x, y):
#     return (x / 100) * y
#
# print(money(suma, podatok))
#-------------------------------------------------------------------------------------------------------------------

# Task 2
# Створіть функцію, яка генерує пароль заданої довжини.
# Функція повинна приймати довжину паролю та булевий параметр, який визначає,
# чи має пароль містити спеціальні символи (наприклад, @, #, $ тощо).
# def passwprds(w, b):
#     lst = []
#     for _ in range(w):
#         if b:
#             lst.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
#         else:
#             lst.append(random.choice(string.ascii_letters + string.digits))
#     return "".join(lst)
#
# print(passwprds(5, False))
#-------------------------------------------------------------------------------------------------------------------

# Task 3
# Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
#  Виведіть значення цього паліндрому і те, множенням яких чисел він є.
# l, p = [], 0
# first, second = 0, 0
# for i in range(100, 999):
#     for j in range(100, 999):
#         if str(j * i) == str(j * i)[::-1] and j * i > p:
#             p = j * i
#             first, second = j, i
# print(f"{p} = {first} x {second}")
#-------------------------------------------------------------------------------------------------------------------

# Task 4
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.
#
#
# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

# задачка  вирішена  ще не до кінця
# def dol_to_word(sum):
#    s_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
#           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', ""]
#    s_2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one hundred']
#    s_3 = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred',
#           'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']
#    if sum <= 20:
#        return s_1[sum-1] + " dollars"
#    elif sum > 20 and sum <= 100:
#        return s_2[sum // 10 - 2] + " " + s_1[sum % 10 - 1] + " dollars"
#    elif sum > 100 and sum <= 120 or sum > 200 and sum <= 220:
#        return s_3[sum // 100 - 1] + " " + s_1[sum % 100 - 1] + " dollars"
#    elif sum > 120 and sum < 200 or sum > 220 and sum < 300:
#        return s_3[sum // 100 - 1] + " " + s_2[sum % 100 // 10 - 2] + " " +  s_1[sum % 10 - 1] + " dollars"
#
#
# print(dol_to_word(287))
