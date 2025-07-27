"""
Configuration settings for the Dental Clinic Analyzer application.
"""

import os
from typing import Optional

class Settings:
    """Application settings and configuration."""
    
    # API Configuration
    GROQ_API_KEY: str = "Your Groq API Key Here"
    GROQ_MODEL: str = "llama3-8b-8192"
    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1/chat/completions"
    
    # Search Configuration
    DEFAULT_MAX_RESULTS: int = 5
    DUCKDUCKGO_BASE_URL: str = "https://html.duckduckgo.com/html/"
    
    # User Agent for web scraping
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    # LLM Configuration
    DEFAULT_TEMPERATURE: float = 0.7
    MAX_COMPLETION_TOKENS: int = 800
    
    @classmethod
    def get_groq_api_key(cls) -> Optional[str]:
        """Get Groq API key from environment or settings."""
        return os.getenv("GROQ_API_KEY", cls.GROQ_API_KEY)

# Create a settings instance
settings = Settings()
