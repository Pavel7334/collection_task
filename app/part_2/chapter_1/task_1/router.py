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
def random_num(num1: int = 1, num2: int = 100):
    value = random.randint(num1, num2)
    return {"number": value}


# 3
"""У вас есть список покупок. Выведите его при обращении на GET /api/1/grocery"""

grocery = ["milk", "sugar", "cookies", "corn-flakes", "nutella"]


@router.get('/api/1/grocery')
def random_grocery():
    return grocery


# 4
"""У вас есть список расходов. Выведите информацию о количестве, сумме, 
максимуме и среднем в ответ на запрос /api/1/grocery-stats"""

grocery_stats = {
    "milk": 150,
    "sugar": 90,
    "cookies": 200,
    "corn-flakes": 140,
    "nutella": 250,
}


@router.get('/api/1/grocery-stats')
def info_expenses():
    count_values = len(grocery_stats.values())
    total = sum(grocery_stats.values())
    maximum = max(grocery_stats.values())
    minimum = min(grocery_stats.values())
    average = sum(grocery_stats.values()) / len(grocery_stats)
    return {
        "count": count_values,
        "total": total,
        "max": maximum,
        "min": minimum,
        "avg": average
    }
