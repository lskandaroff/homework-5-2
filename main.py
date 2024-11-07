# print("Salom Dunyo")
#
# print("2 chi o'zgartirish")
#
# print(" 3 chi ozgartirish")

# Vazifa 5

import re

user_id = 1
while True:
    user_name = input("Ismingizni kiriting: ")
    user_lastname = input("Familyangizni kiriting: ")
    user_age = input("Yoshingizni kiriting: ")
    while True:
        user_phone = input("Tel: ")
        if re.match(r"^\+998\d{9}$", user_phone):
            break
        else:
            print("Telefon raqami noto'g'ri formatda. Iltimos, +998 bilan boshlanadigan telefon raqamini kiriting.")

    user_email = input("Email: ")
    user_adress = input("Adress: ")

    user_data = {
        'id': user_id,
        'name': user_name,
        'lastname': user_lastname,
        'age': user_age,
        'phone': user_phone,
        'email': user_email,
        'address': user_adress
    }

    with open("file.txt", mode="a", encoding="utf-8") as file:
        file.write(f"ID: {user_data['id']}, Name: {user_data['name']}, Lastname: {user_data['lastname']}, "
                       f"Age: {user_data['age']}, Phone: {user_data['phone']}, Email: {user_data['email']}, "
                       f"Address: {user_data['address']}\n")
    user_id += 1


