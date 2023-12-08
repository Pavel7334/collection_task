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


# 4
"""Напишите приложение, которое обрабатывает запросы. В HTTP запросе передаются куки с идентификатором пользователя в формате 

`Cookie: user_pk=3`

У вас есть словарь с информацией о пользователях."""

# users_dict = {
#   1: "Alex",
#   2: "Mary",
#   3: "Danny",
#   4: "Anna",
#   5: "Hanna"
# }


# async def get_user_pk(request: Request):
#     user_pk = request.cookies.get('user_pk')
#     print(request.cookies)
#     if user_pk is None:
#         raise HTTPException(status_code=400, detail="User not found")
#     try:
#         return int(user_pk)
#     except ValueError:
#         raise HTTPException(status_code=400, detail="User not found")
#
#
# @router.get("/user_info/")
# async def get_user_info(request: Request, user_pk: int = Depends(get_user_pk)):
#     user_name = users_dict[user_pk]
#     return {'user_pk': user_pk, 'user_name': user_name}

# 5
"""Напишите приложение, которое обрабатывает запросы. В HTTP запросе передаются куки с идентификатором пользователя 
и его ключом доступа в формате."""

users_dict = [
    {"pk": 1, "email": "alex@mymail.com", "key": "12345"},
    {"pk": 2, "email": "mary@mymail.com", "key": "qwerty9"},
    {"pk": 3, "email": "hanna@mymail.com", "key": "hanna777"}
]


async def get_user_pk(request: Request):
    user_pk = request.cookies.get('user_pk')
    if user_pk is None:
        raise HTTPException(status_code=400, detail="User not found")
    try:
        return int(user_pk)
    except ValueError:
        raise HTTPException(status_code=400, detail="User not found")


@router.get("/user_info2/")
async def get_user_info(request: Request, user_pk: int = Depends(get_user_pk)):
    user_name = users_dict[user_pk]
    return {'user_pk': user_pk, 'user_name': user_name}
