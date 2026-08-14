from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector

app = FastAPI(title="API Usuarios")

# CONFIGURACIÓN MYSQL
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "usuarios_db"
}

def get_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    conn.row_factory = lambda cursor, row: dict(zip([d[0] for d in cursor.description], row))
    return conn

def init_db():
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    conn.commit()
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            edad INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    edad: int

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    edad: Optional[int] = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int

@app.post("/usuarios/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)",
            (usuario.nombre, usuario.email, usuario.edad)
        )
        conn.commit()
        return {"id": cursor.lastrowid, "nombre": usuario.nombre, "email": usuario.email, "edad": usuario.edad}
    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    finally:
        conn.close()

@app.get("/usuarios/", response_model=list[UsuarioResponse])
def obtener_usuarios(skip: int = 0, limit: int = 10):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios LIMIT %s OFFSET %s", (limit, skip))
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    usuario = cursor.fetchone()
    conn.close()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioUpdate):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    update_data = usuario.model_dump(exclude_unset=True)
    if update_data:
        fields = ", ".join([f"{k} = %s" for k in update_data.keys()])
        values = list(update_data.values()) + [usuario_id]
        cursor.execute(f"UPDATE usuarios SET {fields} WHERE id = %s", values)
        conn.commit()
    
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    result = cursor.fetchone()
    conn.close()
    return result

@app.delete("/usuarios/{usuario_id}", status_code=204)
def eliminar_usuario(usuario_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    conn.commit()
    conn.close()
    return None
