# config.py

# Root folder containing all company term sheets
MAIN_FOLDER = "Main_term_sheet"

# Model configuration
GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "llama-3.3-70b-versatile"

# TF-IDF / chunking parameters
TOP_K = 6
CHUNK_SIZE = 2000
OVERLAP = 200

# Prompts file path
PROMPTS_FILE = "Prompts/prompts_term_sheet.json"

#Excel FIle
EXCEL_FILE = "TermSheet Output.xlsx"
