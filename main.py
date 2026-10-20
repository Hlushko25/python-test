
import random
import string


# Функція №1: генерація пароля
def generate_password(length=12):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    return password


# Функція №2: перевірка складності пароля
def check_password(password):
    if len(password) < 8:
        return "Слабкий пароль: менше 8 символів"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([
        has_upper,
        has_lower,
        has_digit,
        has_special
    ])

    if score == 4 and len(password) >= 12:
        return "Високий рівень складності"
    elif score >= 3:
        return "Середній рівень складності"
    else:
        return "Низький рівень складності"


# Функція №3: запис пароля у файл
def save_password(password, filename="passwords.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(password + "\n")

    print(f"Пароль записано у файл {filename}")


# Основна частина програми
length = int(input("Введіть довжину пароля: "))

if length < 1:
    print("Довжина пароля повинна бути додатною!")
else:
    password = generate_password(length)

    print("Згенерований пароль:", password)
    print("Складність:", check_password(password))

    save_password(password)
