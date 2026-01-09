import os
from groq import Groq


def get_groq_client():
    """
    Get Groq API client
    
    Returns:
        Groq client if API key exists, None otherwise
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("⚠️ GROQ_API_KEY not found in environment variables")
        return None  # ✅ Return None, not a string
    
    print(f"✅ Groq API Key loaded: {api_key[:20]}...")
    return Groq(api_key=api_key)


# Debug prints (optional, can remove in production)
if __name__ == "__main__":
    print("CLOUD_NAME:", os.getenv("CLOUDINARY_CLOUD_NAME"))
    print("API_KEY:", os.getenv("CLOUDINARY_API_KEY"))
    print("API_SECRET:", os.getenv("CLOUDINARY_API_SECRET"))
    print("GROQ_API_KEY:", "Found" if os.getenv("GROQ_API_KEY") else "Missing")