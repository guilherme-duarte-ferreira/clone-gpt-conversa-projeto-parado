import sqlite3
from contextlib import contextmanager
import os

DATABASE_PATH = 'data/chat_history.db'

def ensure_data_directory():
    """Garante que o diretório data/ existe"""
    os.makedirs('data', exist_ok=True)

def init_db():
    """Inicializa o banco de dados e cria as tabelas se não existirem"""
    ensure_data_directory()
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                meta JSON
            )
        ''')
        
        db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id)
                ON DELETE CASCADE
            )
        ''')
        db.commit()

@contextmanager
def get_db():
    """Context manager para conexão com o banco"""
    ensure_data_directory()
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()