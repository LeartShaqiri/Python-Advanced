from typing import List, Optional
import sqlite3
from fastapi import APIRouter, HTTPException
from models import Item
from database import get_db_connection


def create_item(item:Item) -> Item:
    conn = get_db_connection()
    cursor = conn.cursor()
    