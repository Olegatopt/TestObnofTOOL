import phonenumbers
from phonenumbers import timezone, geocoder, carrier

print("probv | AH  Привет тебя приветсвует @nicecoolw (это бета тест)")

phoneNumber = (input("Введите номер (+7XXXXXXXXXX):"))

phoneNumber1 = phonenumbers.parse(phoneNumber)

valid = phonenumbers.is_valid_number(phoneNumber1)

timeZone = timezone.time_zones_for_number(phoneNumber1)

Carrier = carrier.name_for_number(phoneNumber1, 'ru')

Region = geocoder.description_for_number(phoneNumber1, 'ru')

print("Рабочий телефон:", valid)
print("Чисовые пояса:", timeZone)
print("Оператор:", Carrier)
print("Регион:", Region)
input()

