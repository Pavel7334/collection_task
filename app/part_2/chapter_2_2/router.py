from fastapi import APIRouter, HTTPException, Header, Depends, Request

router = APIRouter(
    prefix="/pages",
    tags=["Часть 6:"
          " Задачи 1-5"],
)

# 1
"""Напишите приложение, которое обрабатывает запросы к нему.

В HTTP запросе передается заголовок `my_header`

Выведите значение заголовка в теле ответа"""


@router.get("/my_header/")
def get_my_header(my_header: str):
    return my_header


# 2
"""Напишите приложение, которое обрабатывает запросы

В HTTP запросе передается заголовок `From` – этот редко использующийся заголовок предоставляет серверу адрес владельца 

клиента – его электронную почту. Разделите значение заголовка на имя пользователя и почту и выведите в формате JSON.

Если заголовок не отправлен или не содержит `@`, верните ошибку `400`."""


@router.get("/from_header/")
async def read_from_header(from_header: str = Header(None)):
    if not from_header or '@' not in from_header:
        raise HTTPException(status_code=400, detail="Ошибка сервера")

    mail_name, mail_domain = from_header.split('@')
    return {"mail_name": mail_name, "mail_domain": mail_domain}


# 3
"""Напишите приложение, которое обрабатывает запросы.

В HTTP запросе передаются куки.

Выведите куки, которые были переданы в виде словаря."""


async def get_cookie(request: Request):
    return request.cookies


@router.get("/cookies/")
async def get_cookies(cookies: dict = Depends(get_cookie)):
    return cookies







