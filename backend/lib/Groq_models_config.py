# lib/Groq_models_config.py

class ModelConfig:
    """Configure different models for different tasks"""
    
    # 📸 Vision Model (for images)
    VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
    VISION_FALLBACK = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    # 📄 Document Model (for PDFs, Word, Text files)
    DOCUMENT_MODEL = "llama-3.3-70b-versatile"
    DOCUMENT_FALLBACK = "llama-3.1-70b-versatile"
    
    # 💬 General Chat Model (for conversations without files)
    CHAT_MODEL = "llama-3.1-8b-instant"
    CHAT_FALLBACK = "llama-3.3-70b-versatile"
    
    # 🎯 Model settings
    VISION_SETTINGS = {
        "temperature": 0.3,
        "max_tokens": 500
    }
    
    DOCUMENT_SETTINGS = {
        "temperature": 0.2,
        "max_tokens": 1000
    }
    
    CHAT_SETTINGS = {
        "temperature": 0.7,
        "max_tokens": 500
    }

    @staticmethod
    def get_model_for_task(task_type: str) -> dict:
        """Get the appropriate model and settings for a task"""
        if task_type == "vision":
            return {
                "model": ModelConfig.VISION_MODEL,
                "fallback": ModelConfig.VISION_FALLBACK,
                "settings": ModelConfig.VISION_SETTINGS
            }
        elif task_type == "document":
            return {
                "model": ModelConfig.DOCUMENT_MODEL,
                "fallback": ModelConfig.DOCUMENT_FALLBACK,
                "settings": ModelConfig.DOCUMENT_SETTINGS
            }
        elif task_type == "chat":
            return {
                "model": ModelConfig.CHAT_MODEL,
                "fallback": ModelConfig.CHAT_FALLBACK,
                "settings": ModelConfig.CHAT_SETTINGS
            }
        else:
            return {
                "model": ModelConfig.CHAT_MODEL,
                "fallback": ModelConfig.CHAT_FALLBACK,
                "settings": ModelConfig.CHAT_SETTINGS
            }