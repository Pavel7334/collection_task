from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    tags=["Часть 3:"
          " Задачи 1-6"],
)

# 1
"""Создайте приложение, которое при запуске создает глобальную переменную, увеличивайте ее на 1 при каждом POST запросе 
и возвращайте новое значение в обычном текстовом формате. В этом примере мы используем мутабельную переменную, чтобы не 
используем global."""

data = {"value": 1}


@router.post("/value")
async def increase_value():
    data["value"] += 1
    return data


# 2
"""У вас есть список, который хранится в переменной items. Напишите вьюшку, которая добавит элемент 
из json-тела POST запроса и вернет список"""

items = ["alpha", "bravo", "charlie"]


@router.post("/")
async def add_items(new_items: str):
    items.append(new_items)
    return items


# 3
"""У вас есть переменная, где хранится список словарей. Напишите вьюшку, которая добавит элемент 
из json-тела POST запроса и вернет список. """

enrollments = [
    {"name": "alex", "phone": "+123456789"},
]


@router.get("/enrollments")
async def get_enrollments():
    return enrollments


@router.post("/enrollments")
async def add_enrollments(new_enrollments: dict) -> list:
    enrollments.append(new_enrollments)
    return enrollments


# 4
"""У вас есть переменная, где хранится список пользователей. У каждого пользователя есть уникальный идентификатор.
При отправке POST запроса добавьте пользователя в список с очередным pk. Верните словарь с пользователем. """

users_2 = [
    {"pk": 1, "name": "alex", "phone": "+123456789"},
    {"pk": 2, "name": "mary", "phone": "+987654321"}
]


@router.post("/new_users")
async def user(new_user: dict) -> list:
    users_2.append(new_user)
    return users


# 5
"""У вас есть переменная, где хранится список пользователей. При отправке POST запроса проверьте что: - [ ]  имя (name) указано
- [ ]  телефон (phone) указан. Если все ок – добавьте пользователя в список и верните в ответ добавленный словарь.
Если нет – верните список ошибок в формате “name missed”, “phone missed”"""

users = [
    {"name": "alex", "phone": "+123456789"},
    {"name": "mary", "phone": "+987654321"}
]


@router.post("/users")
async def add_user(new_user: dict):
    if "name" not in new_user.keys():
        raise HTTPException(status_code=400, detail="name missed")
    elif "phone" not in new_user.keys():
        raise HTTPException(status_code=400, detail="phone missed")
    elif "" in new_user.keys():
        raise HTTPException(status_code=400, detail="Нет данных")
    users.append(new_user)

    return new_user


# 6
"""У вас есть переменная, где хранится список пользователей. Получите список из тела POST запроса 
и добавьте их в список. Количество пользователей в запросе может быть любым."""


users_3 = [
    {"name": "alex", "phone": "+123456789"},
    {"name": "mary", "phone": "+987654321"}
]


@router.post("/users_3")
async def add_user(new_user: tuple):
    users_3.extend(new_user)
    return users_3

