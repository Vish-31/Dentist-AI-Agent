"""
LLM service for generating marketing insights using Groq API.
"""

import requests
import logging
from typing import Dict, Any, Optional

from config.settings import settings

logger = logging.getLogger(__name__)

class LLMService:
    """Service for interacting with Groq LLM API."""
    
    def __init__(self):
        self.api_key = settings.get_groq_api_key()
        self.model = settings.GROQ_MODEL
        self.base_url = settings.GROQ_BASE_URL
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is required")
    
    def _create_headers(self) -> Dict[str, str]:
        """Create headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _create_marketing_prompt(self, clinic_data: str, your_clinic_name: str) -> str:
        """Create a prompt for marketing analysis."""
        return f"""
I am a dental clinic owner ("{your_clinic_name}"). Below is a list of top clinics nearby:

{clinic_data}

Please do the following:
1. Give 7-10 popular keywords (not full definitions, only keywords) that dentists should use in their marketing content which are different, unique, catchy and sounds good.
2. Suggest 5 unique selling points (USPs) that I can use to differentiate my clinic.
3. Suggest 3 unique marketing strategies and 3 catchy ad slogans to stand out regarding my clinic.

Reply in markdown format.
"""
    
    def analyze_clinics_for_marketing(
        self, 
        clinic_data: str, 
        your_clinic_name: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Analyze clinics and generate marketing insights.
        
        Args:
            clinic_data (str): Data about competitor clinics
            your_clinic_name (str): Name of the user's clinic
            temperature (float): Temperature for LLM generation
            max_tokens (int): Maximum tokens for completion
            
        Returns:
            str: Marketing insights in markdown format
        """
        if temperature is None:
            temperature = settings.DEFAULT_TEMPERATURE
        if max_tokens is None:
            max_tokens = settings.MAX_COMPLETION_TOKENS
        
        prompt = self._create_marketing_prompt(clinic_data, your_clinic_name)
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_completion_tokens": max_tokens
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self._create_headers(),
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "choices" not in data:
                error_msg = data.get("error", "No error message provided.")
                logger.error(f"API error: {error_msg}")
                return f"Failed to generate marketing content. Error: {error_msg}"
            
            content = data["choices"][0]["message"]["content"]
            logger.info("Successfully generated marketing insights")
            return content
            
        except requests.RequestException as e:
            logger.error(f"Request error: {e}")
            return f"Error communicating with API: {e}"
        except KeyError as e:
            logger.error(f"Unexpected API response format: {e}")
            return "Unexpected response format from API."
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return f"Exception during LLM call: {e}"
