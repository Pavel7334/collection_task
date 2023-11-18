from typing import Optional
from fastapi import HTTPException, APIRouter, Response

router = APIRouter(
    tags=["Часть 1:"
          " Задачи 1-10"],
)

alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

# 1
"""Напишите вьюшку для запросов типа /letter/<letter>, которая возвращает букву"""


@router.get("/letter/{letter}")
def letter_view(letter: str):
    result = alphabet.get(letter.upper(), "Not Found")
    if result == "Not Found":
        raise HTTPException(status_code=404, detail="Сервер не найден")

    return {"result": result}


# 2
"""Напишите вьюшку для запросов типа /find/?letter=<letter>, которая возвращает букву на основе квери-параметра."""


@router.get("/find/")
async def find_view(letter: str):
    result = alphabet.get(letter.upper())

    if not result:
        raise HTTPException(status_code=404, detail="Сервер не найден")

    return {"result": result}


# 3
"""Напишите вьюшку для запросов  /check/<letter>/<word> для проверки соответствия буквы ее расшифровке:"""


@router.get("/check/{letter}/{word}")
async def check_view(letter: str, word: str):
    result = alphabet.get(letter.upper())
    return result.lower() == word.lower()


# 4
"""Напишите вьюшку для запросов /between/?from=<letter>&to=<letter> , которая возвращает буквы в промежутке между 
указанными или прочерк, если между указанными буквами ничего нет. """


@router.get("/between/")
async def between_view(from_letter: str, to_letter: str):
    letters = list(alphabet.keys())

    from_index = letters.index(from_letter)
    to_index = letters.index(to_letter)

    if from_index >= to_index:
        return "-", 200

    result = "".join(letters[from_index + 1:to_index])
    return result, 200


# 5
"""Напишите вьюшку для запросов /get-some/<number> которая возвращает указанное количество букв или - если передан 0"""


@router.get("/get-some/{number}")
async def get_some_view(number: int, response: Response):
    letters = "".join(list(alphabet.keys()))
    print(letters)

    result = "".join(letters[:number])

    if not number == 0:
        response.status_code = 200
        return "-"

    return result


# 6
"""Напишите вьюшку для запросов /letters/?limit=<limit>&offset=<offset>, которая возвращает указанное количество букв
 с указанной позиции. Если с таким отступом ничего нет или лимит нулевой – возвращает “-”."""


@router.get("/letters/")
async def letters_view(limit: int, offset: int):
    start = offset
    end = offset + limit
    letters = "abcdefghijklmnopqrstuvwxyz"
    page_letters = letters[start:end]
    print(page_letters)

    if not page_letters:
        return "-", 200

    return page_letters, 200


# 7
"""Напишите вьюшку для запросов /letters/page/<page_number> которая выводила бы по пять элементов, причем, если страница
 не указана, выводятся первые 5 элементов, если же для указанной страницы не хватает элементов, возвращается статус-код 
 404."""


@router.get("/letters/page/{page_number}")
async def letters_view(page_number: Optional[int] = 1):
    start = (page_number - 1) * 5
    end = start + 5
    letters = "abcdefghijklmnopqrstuvwxyz"
    page_letters = letters[start:end]

    if not page_letters:
        raise HTTPException(status_code=404, detail="Not Found")

    return page_letters


# 8
"""Напишите вьюшку для запросов /search/?s=<s> которая бы выводила слова, в которых содержится указанная подстрока. 
Если ничего не нашлось – верните 404."""


@router.get("/search/")
async def search_view(s: str):
    result = [v for k, v in alphabet.items() if s in v]
    print(result)

    if not result:
        raise HTTPException(status_code=404, detail="Not Found")

    return {"result": result}


# 9
"""Напишите вьюшку для запросов /get/?len=<length> которая возвращает все слова указанной длины. 
Если таких слов нет – напишите 404."""


@router.get("/get/")
async def get_view(length: int):
    result = [w for w in alphabet.values() if len(w) == length]
    if not result:
        return {"detail": "Not Found"}, 404
    return {"result": result}


# 10
"""Напишите вьюшку для запросов /letters с  аргументами"""


@router.get("/letters")
async def letters_view(limit: int = None, offset: int = None, sort: str = None):
    if limit is None or offset is None or sort is None or sort not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Bad Request")

    res_str = alphabet[offset:offset+limit]

    if sort == "asc":
        return {"result": res_str}
    else:
        return {"result": res_str[::-1]}


