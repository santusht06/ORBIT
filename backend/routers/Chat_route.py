from fastapi import APIRouter, UploadFile, File, Form, Query, Depends
from sqlalchemy.orm import Session
from controllers.Chat_controller import ChatBot
from lib.Database_config import get_db
from typing import Optional

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
async def unified_chat_endpoint(
    file: Optional[UploadFile] = File(None),
    message: Optional[str] = Form(None),
    action: Optional[str] = Query(None, description="Action: clear_context, get_context, get_history, get_conversations"),
    session_id: Optional[str] = Query(None, description="Conversation session ID (auto-generated if not provided)"),
    db: Session = Depends(get_db)
):
    """
    🎯 UNIFIED CHAT ENDPOINT with Database Persistence
    
    ## Features:
    - **PostgreSQL database** for persistent storage
    - **Conversation tracking** with session_id
    - **Message history** saved automatically
    - **File storage** in database
    - **Multi-model AI** (Vision, Document, Chat)
    
    ## Parameters:
    - `file`: Upload PDF, images, text, Word docs
    - `message`: Your question or message
    - `action`: Special commands (see below)
    - `session_id`: Continue existing conversation (optional)
    
    ## Actions:
    - `clear_context`: Clear file context for session
    - `get_context`: Get current context info
    - `get_history`: Get all messages in conversation
    - `get_conversations`: List all conversations
    
    ## Usage Examples:
    
    ### Start new conversation:
    ```bash
    POST /chat/
    message: "Hello!"
    # Returns session_id - save it for later
    ```
    
    ### Continue conversation:
    ```bash
    POST /chat/?session_id=abc-123-def
    message: "Tell me more"
    ```
    
    ### Upload file:
    ```bash
    POST /chat/?session_id=abc-123-def
    file: document.pdf
    ```
    
    ### Upload and ask:
    ```bash
    POST /chat/?session_id=abc-123-def
    file: report.pdf
    message: "Summarize this"
    ```
    
    ### Get conversation history:
    ```bash
    POST /chat/?action=get_history&session_id=abc-123-def
    ```
    
    ### List all conversations:
    ```bash
    POST /chat/?action=get_conversations
    ```
    """
    
    return await ChatBot.handle_request(
        file=file,
        message=message,
        action=action,
        session_id=session_id,
        db=db
    )