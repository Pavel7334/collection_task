from fastapi import FastAPI

from app.part_1.chapter_1.router import router as router_chapter_1
from app.part_1.chapter_2.router import router as router_chapter_2
from app.part_1.chapter_3.router import router as router_chapter_3
from app.part_1.chapter_4.router import router as router_chapter_4

app = FastAPI(
    title="Сборник задач"
)


app.include_router(router_chapter_1)
app.include_router(router_chapter_2)
app.include_router(router_chapter_3)
app.include_router(router_chapter_4)

