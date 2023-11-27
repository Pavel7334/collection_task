from fastapi import APIRouter

router = APIRouter(
    prefix="/pages",
    tags=["Часть 5:"
          " Задачи 6-10"],
)

data = [
    ("🍏", "Apple Green", "fruit", 45),
    ("🍎", "Apple Red", "fruit", 49),
    ("🍌", "Banana", "fruit", 95),
    ("🥑", "Avocado", "fruit", 160),
    ("🍅", "Tomato", "veggie", 20),
    ("🥦", "Broccoli", "veggie", 34),
    ("🥕", "Carrot", "veggie", 100),
    ("🍪", "Cookie", "sweets", 514),
    ("🍩", "Donut", "sweets", 300),
    ("🍰", "Cake", "sweets", 400),
]

# 6
"""Верните информацию об одном продукте по его имени по запросу"""


@router.get('/api/1/products/{product_name}')
def info_product(product_name):
    for row in data:
        if row[1] == product_name:
            return row
    else:
        return "Такого продукта нет"
