from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.registro_porta_service import add_registro_porta, update_registro_porta, get_registros_porta, delete_registro_porta_by_id
from app.exceptions import DatabaseError

router = APIRouter()


