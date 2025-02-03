from datetime import datetime
import json
import uuid
from backend.database.database import get_db

class Conversation:
    @staticmethod
    def create(title="Nova Conversa"):
        """Cria uma nova conversa"""
        conversation_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        with get_db() as db:
            db.execute(
                'INSERT INTO conversations (id, title, timestamp, meta) VALUES (?, ?, ?, ?)',
                (conversation_id, title, timestamp, '{}')
            )
            db.commit()  # Garante que a conversa seja salva
        return conversation_id

    @staticmethod
    def get_all():
        """Retorna todas as conversas"""
        with get_db() as db:
            cursor = db.execute(
                'SELECT * FROM conversations ORDER BY timestamp DESC'
            )
            return cursor.fetchall()

    @staticmethod
    def get_by_id(conversation_id):
        """Busca uma conversa específica pelo ID"""
        with get_db() as db:
            cursor = db.execute(
                'SELECT * FROM conversations WHERE id = ?',
                (conversation_id,)
            )
            return cursor.fetchone()

    @staticmethod
    def update(conversation_id, title=None, meta=None):
        """Atualiza uma conversa existente"""
        updates = []
        params = []
        
        if title is not None:
            updates.append('title = ?')
            params.append(title)
        if meta is not None:
            updates.append('meta = ?')
            params.append(json.dumps(meta))
            
        if not updates:
            return False
            
        query = f'UPDATE conversations SET {", ".join(updates)} WHERE id = ?'
        params.append(conversation_id)
        
        with get_db() as db:
            db.execute(query, params)
            db.commit()  # Garante que as alterações sejam salvas
            return True

    @staticmethod
    def delete(conversation_id):
        """Deleta uma conversa e suas mensagens"""
        with get_db() as db:
            db.execute('DELETE FROM messages WHERE conversation_id = ?', (conversation_id,))
            db.execute('DELETE FROM conversations WHERE id = ?', (conversation_id,))
            db.commit()  # Garante que a deleção seja efetivada
            return True