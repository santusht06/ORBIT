from sqlalchemy.orm import Session
from models.database_models import Conversation, Message, File, Context, MessageRole, FileType
from typing import Optional, List
import uuid


class ConversationDB:
    """Database operations for conversations"""
    
    @staticmethod
    def create_conversation(db: Session, title: str = "New Conversation") -> Conversation:
        """Create a new conversation"""
        conversation = Conversation(
            session_id=str(uuid.uuid4()),
            title=title
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation
    
    @staticmethod
    def get_conversation(db: Session, session_id: str) -> Optional[Conversation]:
        """Get conversation by session_id"""
        return db.query(Conversation).filter(Conversation.session_id == session_id).first()
    
    @staticmethod
    def get_or_create_conversation(db: Session, session_id: Optional[str] = None) -> Conversation:
        """Get existing conversation or create new one"""
        if session_id:
            conversation = ConversationDB.get_conversation(db, session_id)
            if conversation:
                return conversation
        
        # Create new conversation
        return ConversationDB.create_conversation(db)
    
    @staticmethod
    def get_all_conversations(db: Session, limit: int = 50) -> List[Conversation]:
        """Get all conversations"""
        return db.query(Conversation).order_by(Conversation.updated_at.desc()).limit(limit).all()
    
    @staticmethod
    def delete_conversation(db: Session, session_id: str) -> bool:
        """Delete a conversation"""
        conversation = ConversationDB.get_conversation(db, session_id)
        if conversation:
            db.delete(conversation)
            db.commit()
            return True
        return False


class MessageDB:
    """Database operations for messages"""
    
    @staticmethod
    def create_message(
        db: Session,
        conversation_id: int,
        role: MessageRole,
        content: str,
        model_used: Optional[str] = None,
        mode: Optional[str] = None
    ) -> Message:
        """Create a new message"""
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
            model_used=model_used,
            mode=mode
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message
    
    @staticmethod
    def get_conversation_messages(
        db: Session,
        conversation_id: int,
        limit: Optional[int] = None
    ) -> List[Message]:
        """Get all messages for a conversation"""
        query = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at)
        if limit:
            query = query.limit(limit)
        return query.all()
    
    @staticmethod
    def get_recent_messages(
        db: Session,
        conversation_id: int,
        limit: int = 10
    ) -> List[Message]:
        """Get recent messages for conversation history"""
        return db.query(Message)\
            .filter(Message.conversation_id == conversation_id)\
            .order_by(Message.created_at.desc())\
            .limit(limit)\
            .all()[::-1]  # Reverse to get chronological order


class FileDB:
    """Database operations for files"""
    
    @staticmethod
    def create_file(
        db: Session,
        conversation_id: int,
        filename: str,
        file_type: FileType,
        file_size: Optional[int] = None,
        text_content: Optional[str] = None,
        chunks_count: Optional[int] = None,
        is_image: bool = False,
        image_base64: Optional[str] = None,
        media_type: Optional[str] = None
    ) -> File:
        """Create a new file record"""
        file_record = File(
            conversation_id=conversation_id,
            filename=filename,
            file_type=file_type,
            file_size=file_size,
            text_content=text_content,
            chunks_count=chunks_count,
            is_image=is_image,
            image_base64=image_base64,
            media_type=media_type
        )
        db.add(file_record)
        db.commit()
        db.refresh(file_record)
        return file_record
    
    @staticmethod
    def get_conversation_files(db: Session, conversation_id: int) -> List[File]:
        """Get all files for a conversation"""
        return db.query(File).filter(File.conversation_id == conversation_id).all()
    
    @staticmethod
    def get_latest_file(db: Session, conversation_id: int) -> Optional[File]:
        """Get the most recent file for a conversation"""
        return db.query(File)\
            .filter(File.conversation_id == conversation_id)\
            .order_by(File.created_at.desc())\
            .first()


class ContextDB:
    """Database operations for context chunks"""
    
    @staticmethod
    def save_chunks(db: Session, conversation_id: int, chunks: List[str]):
        """Save text chunks for a conversation"""
        # Delete existing chunks
        db.query(Context).filter(Context.conversation_id == conversation_id).delete()
        
        # Create new chunks
        for index, chunk_text in enumerate(chunks):
            context = Context(
                conversation_id=conversation_id,
                chunk_index=index,
                chunk_text=chunk_text
            )
            db.add(context)
        
        db.commit()
    
    @staticmethod
    def get_chunks(db: Session, conversation_id: int, limit: Optional[int] = None) -> List[str]:
        """Get chunks for a conversation"""
        query = db.query(Context)\
            .filter(Context.conversation_id == conversation_id)\
            .order_by(Context.chunk_index)
        
        if limit:
            query = query.limit(limit)
        
        contexts = query.all()
        return [ctx.chunk_text for ctx in contexts]
    
    @staticmethod
    def clear_chunks(db: Session, conversation_id: int):
        """Clear all chunks for a conversation"""
        db.query(Context).filter(Context.conversation_id == conversation_id).delete()
        db.commit()