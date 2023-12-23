import random
import time
from datetime import datetime
from random import randint

from fastapi import APIRouter, HTTPException, status, Header, Depends, Request, Response

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


# 3
"""Напишите приложение, которое обрабатывает запросы и отдает заголовки.

Создайте в приложении глобальную переменную `request_number = 0`

Напишите вьюшку, которая при каждом новом запросе увеличивала бы значение на  `request_number` на 1. 
В ответ пользователю отправляйте заголовок `Request-Number` с номером текущего запроса."""

request_number = {
    'request_num': 0
}


@router.get('/add_header')
def add_header():
    response = {}
    headers = {'Request-Number': request_number['request_num']}
    request_number['request_num'] += 1
    return response, headers


# 4
"""Напишите вьюшку, которая при каждом запросе сперва создает новую переменную со значением datetime.now(), 
затем ждет случайное количество секунд от 0 до 3, затем считает количество прошедших секунд и возвращает его в заголовке
 Rendering-Time в формате числа с плавающей точкой."""


@router.get('/date_obj')
def date_second(response: Response):
    date_obj = datetime.now()
    time.sleep(randint(0, 3))
    final_time = round((datetime.now() - date_obj).total_seconds(), 2)
    response.headers['Rendering-Time'] = str(final_time)
    return {}


# 5
"""Создайте в приложении глобальную переменную cache_lifetime = 60 означающую время жизни кэша в секундах. 
Напишите вьюшку, которая при запросе GET / отправляет Cache-Control: max_age=60 или другое число, 
записанное  cache_lifetime"""

cache_lifetime = 60


@router.get('/cache_control')
def cache_control(response: Response):
    response.headers['Cache-Control'] = f'max_age = {cache_lifetime}'
    return {}


# 6
"""Напишите вьюшку, которая обрабатывала бы запрос GET /  создавала бы каждый раз случайный реферальный идентификатор 
referal_pk из 10 чисел и устанавливала бы куки с помощью заголовков."""


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


@router.get('/referal_pk')
def referal_pk(response: Response):
    response.headers['Sem-Cook'] = f'referal_pk = {random_with_n_digits(10)}'
    return {}


# 7
"""В POST запросе передаются логин и пароль

У вас есть словарь с информацией о пользователя, где есть почта и пароль.
Обработайте запрос и верните статус код 

`200`, если доступ разрешен

`403`, если доступ запрещен

Если доступ **разрешен**, добавьте в куки `user_pk`"""

dictionary = [
    {"pk": 1, "email": "alex@mymail.com", "password": "12345"},
    {"pk": 2, "email": "mary@mymail.com", "password": "qwerty9"},
    {"pk": 3, "email": "hanna@mymail.com", "password": "hanna777"}
]


@router.post('/info_user')
def info_user(response: Response, pk: int, email: str, password: str):
    for el in dictionary:
        if pk and email and password in el.values():
            response.headers['Sem-Cook'] = f'referal_pk = {pk}'
            return status.HTTP_200_OK
        else:
            return status.HTTP_403_FORBIDDEN


# # 8
# @router.post('/create_files')
# def create_files()



