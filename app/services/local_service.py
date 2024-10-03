from sqlalchemy.orm import Session
from sqlalchemy import text
from app.utils.string_utils import sanitize_string
from app.exceptions import DatabaseError
from app.models import Local

def add_local(db: Session, local: Local):
    db.execute(text(
        "INSERT INTO local (id_categoria, latitude, longitude, nome, endereco) "
        "VALUES (:id_categoria, :latitude, :longitude, :nome, :endereco)"
    ), {
        "id_categoria": local.id_categoria,
        "latitude": local.latitude,
        "longitude": local.longitude,
        "nome": local.nome,
        "endereco": local.endereco
    })
    db.commit()  

def update_local(db: Session, id_local: int, local: Local):
    result = db.execute(text(
        "UPDATE local "
        "SET id_categoria = :id_categoria, "
        "latitude = :latitude, "
        "longitude = :longitude, "
        "nome = :nome, "
        "endereco = :endereco "
        "WHERE id_local = :id_local"
    ), {
        "id_categoria": local.id_categoria,
        "latitude": local.latitude,
        "longitude": local.longitude,
        "nome": local.nome,
        "endereco": local.endereco,
        "id_local": id_local
    })
    db.commit()
    return result.rowcount > 0 

def get_locals(db: Session, where: str = None, limit: int = 100, offset: int = 0):
    try:
        base_query = """
            SELECT 
                id_local, 
                id_categoria, 
                regexp_replace(COALESCE(nome, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS nome,
                regexp_replace(COALESCE(endereco, ''), '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS endereco,
                latitude, 
                longitude
            FROM 
                local 
        """
        
        where_clause = []
        parameters = {}

        if where:
            where_clause.append("unaccent(lower(nome)) LIKE unaccent(lower(:where))")
            parameters["where"] = f"%{where}%"

        if where_clause:
            base_query += " WHERE " + " AND ".join(where_clause)

        base_query += " LIMIT :limit OFFSET :offset"
        parameters["limit"] = limit
        parameters["offset"] = offset

        result = db.execute(text(base_query), parameters)

        return [{
            'id_local': row.id_local,
            'id_categoria': row.id_categoria,
            'nome': row.nome,
            'endereco': row.endereco,
            'latitude': row.latitude,
            'longitude': row.longitude,
        } for row in result]
    except Exception as e:
        raise DatabaseError(f"Erro ao acessar o banco de dados: {str(e)}")

def get_local_by_id(db: Session, id_local: int):
    try:
        base_query = """
            SELECT 
                id_local, 
                id_categoria, 
                latitude, 
                longitude, 
                regexp_replace(nome, '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS nome,
                regexp_replace(endereco, '[^a-zA-Z0-9À-ÿáéíóúãõç ]', '', 'g') AS endereco
            FROM 
                local 
            WHERE 
                id_local = :id_local
        """
        
        result = db.execute(text(base_query), {"id_local": id_local}).fetchone()
        
        if result is None:
            raise ValueError(f"Nenhum local encontrado com o id_local: {id_local}")

        return {
            'id_local': result.id_local,
            'id_categoria': result.id_categoria,
            'latitude': result.latitude,
            'longitude': result.longitude,
            'nome': sanitize_string(result.nome),
            'endereco': sanitize_string(result.endereco),
        }

    except ValueError as ve:
        print(ve)
        return None 
    except Exception as e:
        raise DatabaseError(f"Erro ao acessar o banco de dados: {str(e)}")



def delete_local_by_id(db: Session, id_local: int):
    result = db.execute(text(
        "DELETE FROM local WHERE id_local = :id_local"
    ), {"id_local": id_local})
    db.commit()
    return result.rowcount > 0 