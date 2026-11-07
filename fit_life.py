# Проект FitLife - MVP версия 1.0
print("Добро пожаловать!", "Вас приветствует наша программа FitLife!")
print("Для корректной работы программы, ", "нам нужно узнать несколько информации о вас!\n")


user_name = input("Как вас зовут? ... ").capitalize()  # спрашиваем имя, в любом случае сохраняя первую букву заглавной

user_age = int(input("Сколько вам лет? (например 20) ... "))  # возраст как int

print("\nОтлично, ещё пару вопросиков.\n")


user_weight = float(input("Какой у вас вес? (в кг, например 60.5) ... "))  # вес как float

user_height = float(input("Какой у вас рост? (в метрах, например 1.75) ... "))  # рост как float
if user_height >= 100:  # проверка на возможное недопонимание
    user_height = user_height / 100
    print(f"Вы вероятно имели ввиду {user_height}, ",  "так как ответ в метрах, а не сантиметрах.")

print("\nОтлично, опрос окончен, подсчитываем...\n")


# подсчёт ИМТ функцией
def calculate_bmi(weight, height): 
    return weight / (height ** 2)

bmi = round(calculate_bmi(user_weight, user_height), 1)
# подсчёт нормы воды функцией
def calculate_water(weight):
    return weight * 30

water_needed_ml = calculate_water(user_weight)
water_needed_l = round(water_needed_ml / 1000, 2)  # преобразование в литры + округление


print(f"Результаты готовы, {user_name}!", f"Так как вам {user_age} лет, ", "вот ваши округленные данные и нормы: ")
print(f"    - Индекс Массы Тела (ИМТ) {bmi}\n", f"    - Рекомендуемая норма воды в литрах {water_needed_l}\n")
print("Расчет окончен. Будьте здоровы!")