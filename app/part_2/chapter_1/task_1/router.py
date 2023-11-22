import random
from fastapi import APIRouter

router = APIRouter(
    prefix="/pages",
    tags=["Часть 5:"
          " Задачи 1-6"],
)

# 1
"""Создайте приложение, которое при обращении на /api/1/random вернет случайное число от 1 до 10 в виде {”number”: N}"""


@router.get('/api/1/random/')
def view_random():
    value = random.randint(1, 10)
    return {"number": value}


# 2
"""Создайте приложение, которое при обращении на /api/1/random?from=…&to=… вернет случайное число от X до Y в виде 
{”number”: N}. Если параметры from и to не заданы, их значения по умолчанию 1 и 100 соответственно."""


@router.get('/api/1/random')
def random_num(num1=None, num2=None):
    if num1 is None and num2 is None:
        value = random.randint(1, 100)
        return {"number": value}
    else:
        value = random.randint(int(num1), int(num2))
        return {"number": value}


# 3
"""У вас есть список покупок. Выведите его при обращении на GET /api/1/grocery"""

grocery = ["milk", "sugar", "cookies", "corn-flakes", "nutella"]


@router.get('/api/1/grocery')
def random_grocery():
    return grocery
