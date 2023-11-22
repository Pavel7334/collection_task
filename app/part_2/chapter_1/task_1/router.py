import random
from fastapi import APIRouter

router = APIRouter(
    prefix="/pages",
    tags=["Часть 5:"
          " Задачи 1-6"],
)


@router.get('/api/1/random/')
def view_random():
    value = random.randint(1, 10)
    return {"number": value}


@router.get('/api/1/random')
def random_num(num1=None, num2=None):
    if num1 is None and num2 is None:
        value = random.randint(1, 100)
        return {"number": value}
    else:
        value = random.randint(int(num1), int(num2))
        return {"number": value}
