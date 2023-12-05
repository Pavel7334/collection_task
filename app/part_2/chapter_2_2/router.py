from fastapi import APIRouter

router = APIRouter(
    prefix="/pages",
    tags=["Часть 6:"
          " Задачи 1-5"],
)

# 1
"""Напишите приложение, которое обрабатывает запросы к нему.

В HTTP запросе передается заголовок `my_header`

Выведите значение заголовка в теле ответа"""


@router.get("/")
async def get_my_header(my_header: str):
    return my_header
