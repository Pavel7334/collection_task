from fastapi import APIRouter

router = APIRouter(
    prefix="/pages",
    tags=["Часть 6:"
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
        if row[1] == product_name.capitalize():
            return row
    else:
        return "Такого продукта нет"


# 7
"""Верните все продукты в категории в виде списка. Если категория не указана – верните вообще все. 
GET /api/1/products/?cat=<cat>"""


@router.get('/api/1/products/')
def get_product(product_cat):
    list_cat = []
    for row in data:
        if row[2] == product_cat:
            list_cat.append(row)
    return list_cat or data


# 8
"""Верните  все продукты с килокалориями в выбранном диапазоне. Если указано только от – фильтруйте от 
него до бесконечности. Если указано только до – фильтруйте от 0 и до него. Если диапазон не указан - верните все."""


@router.get('/api/2/products/')
def get_kcal(kcal_from: int = 0, kcal_to: int = 10000):
    return [row for row in data if row[-1] > kcal_from and row[-1] < kcal_to]


    # list_kcal_from = []
    # for row in data:
    #     if row[3] in range(kcal_from, kcal_to):
    #         list_kcal_from.append(row)
    # return list_kcal_from


# 9
"""Верните все категории из списка. GET /api/1/categories"""


@router.get('/api/1/categories')
def get_category():
    new_lst = []
    for row in data:
        if row[2] not in new_lst:
            new_lst.append(row[2])
    return new_lst


# 10
"""Верните по запросу GET /api/1/get_products/1_2_3 список продуктов с соответствующими ключами. 
Если какого-то ключа нет – пропускаем"""


# @router.get('/api/1/get_products/')
# def gey_products():
#


