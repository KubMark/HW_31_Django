import datetime

from dateutil.relativedelta import relativedelta # Делаем расчеты разницы дат
from rest_framework.exceptions import ValidationError

"""Делаем проверку возраста пользователя не менее 9 лет при регистрации"""


def check_birth_date(birth_date):
    year_diff = relativedelta(datetime.date.today(), birth_date).years
    if year_diff < 9:
        raise ValidationError(f"У пользователя возраст {year_diff} лет! Разрешено только с 9-ти!")


"""Делаем проверку Email и запрещаем если это  rambler.ru"""


def check_email(email):
    if "rambler.ru" in email.split("@")[-1]:
        raise ValidationError(f"Регистрация с домена rambler.ru запрещена!")
