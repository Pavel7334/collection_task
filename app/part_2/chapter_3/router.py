from fastapi import APIRouter, HTTPException, Header, Depends, Request, Response

router = APIRouter(
    prefix="/pages",
    tags=["Часть 8:"
          " Задачи 1-7"],
)

# 1
"""Напишите приложение, которое  при запросе GET / возвращала бы в ответе заголовок Server-Environment со 
значением development. Тело ответа оставьте пустым."""


@router.get("/index/")
def index(response: Response):
    response.headers["Server-Environment"] = "development"
    return ""

