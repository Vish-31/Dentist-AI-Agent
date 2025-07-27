# Dental Clinic Marketing Analyzer

A Streamlit application that helps dental clinic owners analyze their competition and get AI-powered marketing insights.

## Features

- 🔍 **Competitor Search**: Find top dental clinics in your area
- 🧠 **AI Marketing Insights**: Get personalized marketing suggestions using Groq LLM
- 🎯 **SEO Keywords**: Discover popular keywords for dental marketing
- 💡 **USPs**: Get unique selling points to differentiate your clinic
- 📈 **Marketing Strategies**: Receive tailored marketing strategies and catchy slogans

## Project Structure

```
Assisstant/
├── main.py                 # Main entry point
├── app.py                  # Original monolithic app (can be removed)
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuration and API keys
├── services/
│   ├── __init__.py
│   ├── search_service.py  # DuckDuckGo search functionality
│   └── llm_service.py     # Groq LLM integration
├── utils/
│   ├── __init__.py
│   └── helpers.py         # Utility functions
└── src/
    ├── __init__.py
    └── ui.py              # Streamlit UI components
```

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open `config/settings.py`
2. Update the `GROQ_API_KEY` with your actual API key
3. Alternatively, set the `GROQ_API_KEY` environment variable

## Usage

Run the application using:

```bash
streamlit run main.py
```

Then:
1. Enter your clinic name
2. Enter your location
3. Click "Analyze Nearby Clinics"
4. View competitor clinics and marketing insights

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key (optional if set in settings.py)

## Dependencies

- `streamlit`: Web application framework
- `requests`: HTTP library for API calls
- `beautifulsoup4`: HTML parsing for web scraping
- `lxml`: XML/HTML parser

## License

This project is for educational and commercial use.
