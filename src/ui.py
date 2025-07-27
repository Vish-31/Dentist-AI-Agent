"""
Streamlit UI components for the Dental Clinic Analyzer.
"""

import streamlit as st
from typing import List, Tuple

from services import SearchService, LLMService
from utils import format_clinic_data, validate_inputs

class DentalAnalyzerUI:
    """Main UI class for the Dental Clinic Analyzer."""
    
    def __init__(self):
        self.search_service = SearchService()
        self.llm_service = LLMService()
    
    def setup_page(self):
        """Set up the Streamlit page configuration."""
        st.set_page_config(
            page_title="Dental Clinic Analyzer", 
            layout="centered",
            page_icon="🦷"
        )
        st.title("🦷 Dental Marketing Analyzer")
        st.write("Find local competitors and get marketing suggestions!")
    
    def render_input_form(self) -> Tuple[str, str]:
        """
        Render the input form for clinic name and location.
        
        Returns:
            Tuple[str, str]: clinic name and location
        """
        col1, col2 = st.columns(2)
        
        with col1:
            clinic_name = st.text_input(
                "Your Clinic Name", 
                placeholder="e.g. SmileBright Dental",
                help="Enter the name of your dental clinic"
            )
        
        with col2:
            location = st.text_input(
                "Location", 
                placeholder="e.g. Bangalore",
                help="Enter the city or area to search for competitors"
            )
        
        return clinic_name, location
    
    def display_search_results(self, results: List[Tuple[str, str]]):
        """Display the search results."""
        st.subheader("🔍 Top Clinics Found")
        
        if not results:
            st.warning("No clinics found. Try a different location.")
            return
        
        for i, (title, link) in enumerate(results, 1):
            st.markdown(f"{i}. [{title}]({link})")
    
    def display_marketing_insights(self, analysis: str):
        """Display the marketing insights."""
        st.markdown("---")
        st.subheader("💡 Marketing Insights")
        
        if "Failed to generate" in analysis or "Error" in analysis:
            st.error("Failed to generate marketing insights. Please try again.")
            st.text(analysis)
        else:
            st.markdown(analysis)
    
    def run(self):
        """Run the main application."""
        self.setup_page()
        
        # Input form
        clinic_name, location = self.render_input_form()
        
        # Analysis button
        if st.button("🔍 Analyze Nearby Clinics", type="primary"):
            if not validate_inputs(clinic_name, location):
                st.warning("⚠️ Please fill in both the clinic name and location.")
                return
            
            # Search for clinics
            with st.spinner("🔍 Searching nearby clinics..."):
                results = self.search_service.search_dental_clinics(location)
            
            if not results:
                st.warning("No clinics found. Try a different location.")
                return
            
            # Display search results
            self.display_search_results(results)
            
            # Generate marketing insights
            with st.spinner("🧠 Analyzing for marketing insights..."):
                clinic_data = format_clinic_data(results)
                analysis = self.llm_service.analyze_clinics_for_marketing(
                    clinic_data, 
                    clinic_name
                )
            
            # Display insights
            self.display_marketing_insights(analysis)
        
        # Add sidebar with additional information
        self._render_sidebar()
    
    def _render_sidebar(self):
        """Render the sidebar with additional information."""
        with st.sidebar:
            st.header("ℹ️ About")
            st.write("""
            This tool helps dental clinic owners:
            
            • **Find competitors** in their area
            • **Get marketing keywords** for better SEO
            • **Discover USPs** to differentiate their clinic
            • **Generate marketing strategies** and slogans
            
            Simply enter your clinic name and location to get started!
            """)
            
            st.header("🛠️ Features")
            st.write("""
            - Real-time competitor search
            - AI-powered marketing insights
            - SEO keyword suggestions
            - Unique selling points
            - Marketing strategies
            - Catchy ad slogans
            """)
