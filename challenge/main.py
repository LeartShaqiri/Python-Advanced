from fastapi import FastAPI
from database import init_db
from routers import category_router, recipe_router

app = FastAPI(
    title="Recipe & Category API",
    description="A REST API for managing recipes and categories.",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(category_router)
app.include_router(recipe_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Recipe API. Visit /docs for the interactive documentation."}