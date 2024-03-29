from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/pages",
    tags=["Часть 9:"
          " Задачи 1-8"],
)

cities = [
    {"pk": 1, "Sydney": "public"},
    {"pk": 2, "Venice": "hidden"},
    {"pk": 3, "Los Angeles": "removed"},
    {"pk": 4, "Tokyo": "public"},
    {"pk": 5, "Rome": "public"}
]

# 1
"""Напишите приложение, которое обрабатывает запросы типа `/location/<pk>`

Если по указанному номеру есть город, сервер возвращает название города в формате JSON, например `{”location”: “Rome”}` 
и код `200`

Если по указанному номеру города нет, сервер возвращает сообщение `{’error’: “not found”}` и статус-код `404`

Статус не учитывается при выводе и все города выводятся."""


@router.get("/location/{pk}")
async def get_location(pk: int):
    for city in cities:
        if city['pk'] == pk:
            return {"location": list(city)[1]}
            # return {"location": list(city)[1]}, HTTPException(status_code=200)

    raise HTTPException(status_code=404, detail="Item not found")


# 2
"""Напишите приложение, которое обрабатывает запросы `GET` запросы  `/location/<pk>`

Если по указанному номеру есть город и его статус – public, сервер возвращает название города в формате JSON, 

например `{”location”: “Rome”}` и код `200`

Если город есть, но его статус hidden или removed, сервер возвращает сообщение `{’error’: “no access”}` и код `403`

Если по указанному номеру города нет,  сервер возвращает сообщение `{’error’: “not found”}` и код `404`"""


@router.get("/location_pk/{pk}")
async def get_location_pk(pk: int):
    for city in cities:
        if city['pk'] == pk:
            if 'public' in city.values():
                return {"location": list(city)[1]}
            raise HTTPException(status_code=403, detail="Forbidden")
    raise HTTPException(status_code=404, detail="Item not found")
