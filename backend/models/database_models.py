from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from lib.Database_config import Base
import enum


class FileType(str, enum.Enum):
    """File type enum"""
    IMAGE = "image"
    PDF = "pdf"
    WORD = "word"
    TEXT = "text"
    UNKNOWN = "unknown"


class MessageRole(str, enum.Enum):
    """Message role enum"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Conversation(Base):
    """
    Conversation/Session table
    Represents a chat session
    """
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(255), unique=True, index=True, nullable=False)
    title = Column(String(500), default="New Conversation")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")
    files = relationship("File", back_populates="conversation", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Conversation {self.session_id}>"


class Message(Base):
    """
    Message table
    Stores all chat messages
    """
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role = Column(Enum(MessageRole), nullable=False)
    content = Column(Text, nullable=False)
    model_used = Column(String(255), nullable=True)  # Which AI model was used
    mode = Column(String(100), nullable=True)  # chat, document_analysis, image_analysis
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    conversation = relationship("Conversation", back_populates="messages")

    def __repr__(self):
        return f"<Message {self.id} - {self.role}>"


class File(Base):
    """
    File table
    Stores uploaded files metadata
    """
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    filename = Column(String(500), nullable=False)
    file_type = Column(Enum(FileType), nullable=False)
    file_size = Column(Integer, nullable=True)  # Size in bytes
    cloudinary_url = Column(String(1000), nullable=True)  # If stored in Cloudinary
    
    # For text-based files
    text_content = Column(Text, nullable=True)
    chunks_count = Column(Integer, nullable=True)
    
    # For images
    is_image = Column(Boolean, default=False)
    image_base64 = Column(Text, nullable=True)  # Base64 encoded image
    media_type = Column(String(100), nullable=True)  # image/jpeg, image/png, etc.
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    conversation = relationship("Conversation", back_populates="files")

    def __repr__(self):
        return f"<File {self.filename}>"


class Context(Base):
    """
    Context table
    Stores current active context/chunks for each conversation
    """
    __tablename__ = "contexts"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    chunk_index = Column(Integer, nullable=False)  # Order of chunks
    chunk_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Context chunk {self.chunk_index}>"