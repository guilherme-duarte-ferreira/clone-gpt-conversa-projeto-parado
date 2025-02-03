from datetime import datetime
import uuid
from backend.database.database import get_db

class Message:
    @staticmethod
    def create(conversation_id, role, content):
        """Cria uma nova mensagem"""
        message_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        with get_db() as db:
            db.execute(
                'INSERT INTO messages (id, conversation_id, role, content, timestamp) VALUES (?, ?, ?, ?, ?)',
                (message_id, conversation_id, role, content, timestamp)
            )
        return message_id

    @staticmethod
    def get_by_conversation(conversation_id):
        """Retorna todas as mensagens de uma conversa"""
        with get_db() as db:
            cursor = db.execute(
                'SELECT * FROM messages WHERE conversation_id = ? ORDER BY timestamp ASC',
                (conversation_id,)
            )
            return cursor.fetchall()

    @staticmethod
    def get_by_id(message_id):
        """Busca uma mensagem específica pelo ID"""
        with get_db() as db:
            cursor = db.execute(
                'SELECT * FROM messages WHERE id = ?',
                (message_id,)
            )
            return cursor.fetchone()