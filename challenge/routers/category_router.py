from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, DBCategory
from models import CategoryCreate, Category

router = APIRouter(prefix="/categories", tags=["Categories"])


def get_category_or_404(category_id: int, db: Session) -> DBCategory:
    category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=List[Category])
def get_categories(db: Session = Depends(get_db)):
    """Retrieves all categories from the database."""
    return db.query(DBCategory).all()


@router.post("/", response_model=Category, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """Creates a new category in the database."""
    db_category = DBCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    """Updates the name of an existing category by its ID."""
    db_category = get_category_or_404(category_id, db)
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Deletes a category from the database by its ID."""
    db_category = get_category_or_404(category_id, db)
    db.delete(db_category)
    db.commit()
    return {"detail": "Category has been deleted"}