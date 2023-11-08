from fastapi import APIRouter

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



