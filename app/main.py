from fastapi import FastAPI

from app.chapter_1.router import router as router_chapter_1

app = FastAPI(
    title="Сборник задач"
)


app.include_router(router_chapter_1)