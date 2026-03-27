from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, DBRecipe
from models import RecipeCreate, Recipe

router = APIRouter(prefix="/recipes", tags=["Recipes"])


def get_recipe_or_404(recipe_id: int, db: Session) -> DBRecipe:
    recipe = db.query(DBRecipe).filter(DBRecipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.get("/", response_model=List[Recipe])
def get_recipes(db: Session = Depends(get_db)):
    """Retrieves all recipes from the database."""
    return db.query(DBRecipe).all()


@router.get("/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """Retrieves a single recipe by its ID."""
    return get_recipe_or_404(recipe_id, db)


@router.post("/", response_model=Recipe, status_code=201)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    """Creates a new recipe in the database."""
    db_recipe = DBRecipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate, db: Session = Depends(get_db)):
    """Updates an existing recipe by its ID."""
    db_recipe = get_recipe_or_404(recipe_id, db)
    for key, value in recipe.model_dump().items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """Deletes a recipe from the database by its ID."""
    db_recipe = get_recipe_or_404(recipe_id, db)
    db.delete(db_recipe)
    db.commit()
    return {"detail": "Recipe has been deleted"}