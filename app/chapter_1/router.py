from fastapi import HTTPException, APIRouter

router = APIRouter(
  tags=["Задачт 1-10"],
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


"""Напишите вьюшку для запросов типа /letter/<letter>, которая возвращает букву"""


@router.get("/letter/{letter}")
def letter_view(letter: str):
    result = alphabet.get(letter.upper(), "Not Found")
    if result == "Not Found":
        raise HTTPException(status_code=404, detail="Сервер не найден")

    return {"result": result}


"""Напишите вьюшку для запросов типа /find/?letter=<letter>, которая возвращает букву на основе квери-параметра."""


@router.get("/find/")
async def find_view(letter: str):

    result = alphabet.get(letter.upper())

    if not result:
        raise HTTPException(status_code=404, detail="Not Found")

    return {"result": result}
