from fastapi import APIRouter, HTTPException, Header, Depends, Request, Response

router = APIRouter(
    prefix="/pages",
    tags=["Часть 8:"
          " Задачи 1-7"],
)

# 1
"""Напишите приложение, которое  при запросе GET / возвращала бы в ответе заголовок Server-Environment со 
значением development. Тело ответа оставьте пустым."""


@router.get("/index_head/")
def index(response: Response):
    response.headers["Server-Environment"] = "development"
    return ""


# 2
"""Напишите приложение, которое обрабатывает запросы и отдает заголовки.

Создайте в приложении глобальную переменную или конфиг `server_environment` по умолчанию установленную в development.  
Напишите вьюшку, которая при запросе `GET /` возвращала бы заголовок `Server-Environment`  
с записанным  в переменной  `server_environment` значением."""


server_environment = 'development'


@router.get('/index_header')
async def index():
    response = {}
    headers = {'Server-Environment': server_environment}
    return response, headers


