"""
Utility functions for the Dental Clinic Analyzer application.
"""

import logging
from typing import List, Tuple

def setup_logging(log_level: str = "INFO") -> None:
    """Set up logging configuration."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

def format_clinic_data(results: List[Tuple[str, str]]) -> str:
    """
    Format clinic search results for LLM analysis.
    
    Args:
        results: List of (title, link) tuples
        
    Returns:
        str: Formatted clinic data
    """
    return "\n".join([f"- {title}: {link}" for title, link in results])

def validate_inputs(clinic_name: str, location: str) -> bool:
    """
    Validate user inputs.
    
    Args:
        clinic_name: Name of the clinic
        location: Location to search
        
    Returns:
        bool: True if inputs are valid
    """
    return bool(clinic_name and clinic_name.strip() and location and location.strip())
