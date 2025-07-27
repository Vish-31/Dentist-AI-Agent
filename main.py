"""
Main entry point for the Dental Clinic Analyzer application.
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src import DentalAnalyzerUI
from utils import setup_logging

def main():
    """Main application entry point."""
    # Setup logging
    setup_logging()
    
    # Create and run the UI
    app = DentalAnalyzerUI()
    app.run()

if __name__ == "__main__":
    main()
