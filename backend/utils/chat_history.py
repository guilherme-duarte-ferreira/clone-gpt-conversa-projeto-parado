from backend.models.conversations import Conversation
from backend.models.messages import Message

def save_conversation(message, response, conversation_id=None):
    """
    Salva ou atualiza uma conversa no banco de dados.
    Se conversation_id for fornecido, adiciona mensagens à conversa existente.
    Caso contrário, cria uma nova conversa.
    """
    if not conversation_id:
        conversation_id = Conversation.create()
        
    Message.create(conversation_id, 'user', message)
    Message.create(conversation_id, 'assistant', response)
    
    return conversation_id

def get_conversation_history():
    """Retorna o histórico completo de conversas"""
    conversations = Conversation.get_all()
    history = []
    
    for conv in conversations:
        messages = Message.get_by_conversation(conv['id'])
        history.append({
            'id': conv['id'],
            'timestamp': conv['timestamp'],
            'messages': [dict(msg) for msg in messages]
        })
    
    return history

def get_conversation_by_id(conversation_id):
    """Busca uma conversa específica com suas mensagens"""
    conversation = Conversation.get_by_id(conversation_id)
    if not conversation:
        return None
        
    messages = Message.get_by_conversation(conversation_id)
    return {
        'id': conversation['id'],
        'timestamp': conversation['timestamp'],
        'messages': [dict(msg) for msg in messages]
    }