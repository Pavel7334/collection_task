from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Часть 4:"
          " Задачи 1-6"],
)

# 1
"""Напишите шаблон, который выводит в виде HTML информацию об одном рейсе. 
В шаблон передаются переменные: departure_airport, arrival_airport, departure_time, arrival_time."""

flight_number = 'SU123'
aircraft = 'Airbus A320'

departure_time = '14:30'
arrival_time = '18:45'

departure_airport = 'SVO'
arrival_airport = 'JFK'

templates = Jinja2Templates(directory='app/part_1/chapter_4/templates')


@router.get('/items', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('item.html', {
        'request': request,
        'departure_airport': departure_airport,
        'arrival_airport': arrival_airport,
        'departure_time': departure_time,
        'arrival_time': arrival_time
    })


# 2
"""Напишите шаблон, который выводит в виде HTML информацию об одном аэропорте."""

airport = {
    'code': 'LHR',
    'name': 'Heathrow',
    'runways': 2,
    'country': 'Великобритания',
    'city': 'Лондон'
}


@router.get("/airport", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("airport.html", {"request": request, "airport": airport})


# 3
"""Напишите шаблон, который выводит в виде HTML информацию об одном самолете.
Обратите внимание, данные содержат вложенные поля."""

aircraft_1 = {
    'model': 'Airbus A380',
    'year': 2007,
    'crew': 3,
    'airline': {
        'name': 'Emirates',
        'country': 'ОАЭ'
    }
}


@router.get('/aircraft', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('aircraft.html', {'request': request, 'aircraft_1': aircraft_1})


# 4
"""Напишите шаблон, который выводит в виде HTML информацию о билете.
Обратите внимание, данные содержат вложенные поля."""

ticket = {
    'seat': '12A',
    'class': 'economy',

    'passenger': {'name': 'John Smith', },

    'aircraft': {'model': 'Boeing 737', },

    'flight': {
        'departure_time': '10:00',
        'arrival_time': '12:30'
    }
}


@router.get('/ticket', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('ticket.html', {'request': request, 'ticket': ticket})


# 5
"""Напишите шаблон, который выводит в виде HTML информацию о погоде и вылете."""

flight = {
    'aircraft': {'model': 'Boeing 737', },
    'shedule': {
        'departure_time': '10:00',
        'arrival_time': '12:30'
    }
}

weather = {
    'wind_speed': 12,
    'visibility': 1400,
    'temp': 15
}


@router.get('/weather_departure', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('weather_departure.html', {
        'request': request,
        'weather': weather,
        'flight': flight
    })


# 6
"""Напишите шаблон, который выведет информацию о рейсе и покажет сообщение с новым временем, если рейс был задержан."""

delayed = {
    "flight_number": "SU123",
    "aircraft": "Airbus A320",

    "departure_time": "14:30",
    "departure_airport": "SVO",

    "arrival_time": "18:45",
    "arrival_airport": "MSQ",

    "delayed": False,
    "new_departure_time": "15:10",
    "new_arrival_time": "19:20",
}
not_delayed = {
    "flight_number": "SU123",
    "aircraft": "Airbus A320",

    "departure_time": "14:30",
    "departure_airport": "SVO",

    "arrival_time": "18:45",
    "arrival_airport": "MSQ",
}


@router.get('/info_flight', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('info_flight.html', {
        'request': request,
        'delayed': delayed,
        'not_delayed': not_delayed})

