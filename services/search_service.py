"""
Search service for finding dental clinics using DuckDuckGo.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
import logging

from config.settings import settings

logger = logging.getLogger(__name__)

class SearchService:
    """Service for searching dental clinics online."""
    
    def __init__(self):
        self.headers = {"User-Agent": settings.USER_AGENT}
    
    def search_duckduckgo(self, query: str, max_results: int = None) -> List[Tuple[str, str]]:
        """
        Search for dental clinics using DuckDuckGo.
        
        Args:
            query (str): Search query
            max_results (int): Maximum number of results to return
            
        Returns:
            List[Tuple[str, str]]: List of (title, link) tuples
        """
        if max_results is None:
            max_results = settings.DEFAULT_MAX_RESULTS
            
        try:
            url = f"{settings.DUCKDUCKGO_BASE_URL}?q={query.replace(' ', '+')}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            
            for result in soup.find_all("a", class_="result__a", limit=max_results):
                title = result.get_text().strip()
                link = result.get("href", "")
                if title and link:
                    results.append((title, link))
                    
            logger.info(f"Found {len(results)} results for query: {query}")
            return results
            
        except requests.RequestException as e:
            logger.error(f"Error searching DuckDuckGo: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error in search: {e}")
            return []
    
    def search_dental_clinics(self, location: str, max_results: int = None) -> List[Tuple[str, str]]:
        """
        Search for dental clinics in a specific location.
        
        Args:
            location (str): Location to search in
            max_results (int): Maximum number of results
            
        Returns:
            List[Tuple[str, str]]: List of (title, link) tuples
        """
        query = f"top dental clinics in {location}"
        return self.search_duckduckgo(query, max_results)
