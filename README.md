# SFI Data Information Extractor

A comprehensive pipeline for extracting, parsing, and structuring textual and tabular data from corporate PDFs, including SPO (Second Party Opinion) reports, frameworks, and term sheets. The project outputs a ready-to-use Excel sheet for further analysis.

---

## Project Structure

### Main Folders

- **Main_spo_framework/**: Contains subfolders for each company.  
  Each subfolder should contain **exactly two PDF files**:
  - Framework PDF
  - Second Party Opinion PDF  

  PDFs can be in any order, but the preferred order is framework first, SPO second.

- **Main_term_sheet/**: Contains PDFs for term sheets. The structure is similar to SPO framework PDFs.

### Code Pipelines

The project consists of **two main pipelines**:

#### 1. Textual Data Pipeline

- **Files**:
  - `extractor.py`: Extracts textual data from PDFs using Python built-in libraries.
  - `parser.py`: Breaks text into chunks, builds a vector database, and parses using a Large Language Model (LLM) via API key.
  - `writer.py`: Structures the LLM output and writes it to an Excel sheet.
  - `main.py`: Orchestrates the textual pipeline by calling all functions sequentially.
  
- **Prompts**: Stored in `Prompts/prompts_spo_framework.json`. They guide the LLM in extracting structured JSON output.

- **Workflow**:
  1. Read all PDFs from `Main_spo_framework`.
  2. Extract textual data for all subfolders.
  3. Parse textual data using LLM.
  4. Write structured output to Excel.

#### 2. Tabular Data Pipeline

- **Files**:
  - `table_extractor.py`: Extracts tables from PDFs using LLMWhisperer.
  - `table_parser.py`: Uses LLM to process tables as context (no chunking to avoid data loss).
  - `table_writer.py`: Writes structured tabular output to Excel.
  - `main.py`: Calls functions for the tabular pipeline.
  
- **Prompts**: Stored in `Prompts/prompts_table.json`.

- **Workflow**:
  1. Extract tables for all PDFs.
  2. Parse the table data using LLM.
  3. Write the entire structured output to Excel.

**Note**: Unlike textual data, for tabular data the entire dataset is extracted first and then written.

---

## Term Sheets

- Works similarly to the SPO and framework pipeline.
- Prompts are located in `Prompts/prompts_term_sheet/`.
- Main script: `Python_term_sheet/main.py`.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)
- API Keys: (depending on what to work with)
  - `LLMWhisperer API Key`
  - `OpenAI API Key`
  - `Gemini API Key`
  - `Groq API Key`

  
---

### Installation & Quick Start

1. **Clone the repository**:

```bash
git clone https://github.com/CandyButcher27/SFI-Data-Project.git
cd SFI-Data-Project
```
### 2. **Create a Virtual Envoirnemnt** :

```bash
# Windows
python -m venv venv

# Mac/Linux
python3 -m venv venv
```
### 3. **Activate the Virtual Envoirnment**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```
### 4. **Install dependencies**
```bash
pip install -r requirements.txt
```
### 5. **Set Environment Variables**
```bash
# Mac/Linux
export LLMWHISPERER_API_KEY='your_api_key'
export OPENAI_API_KEY='your_api_key'

# Windows (CMD)
set LLMWHISPERER_API_KEY='your_api_key'
set OPENAI_API_KEY='your_api_key'
```
### 6. **Run the PipeLine**
```bash
#SPO and Framework
cd Python_spo_framework
python main.py

#Term Sheets
cd Python_term_sheet
python main.py
```

### Output :  Excel sheets containing structured textual and tabular data.

### Documentation

The project documentation is generated using Doxygen.

- **Web version:** 
[Frameworks and SPOs](https://candybutcher27.github.io/SFI-Data-Project/)(Hosted via Github Pages)
  
- **To regenerate documentation locally:**  
  1. Make sure Doxygen is installed.  
  2. Navigate to the project folder in terminal:
     ```bash
     cd Python_spo_framework
     ```
  3. Run:
     ```bash
     doxygen Doxyfile
     ```
- **Notes:**  
  - Only `docs/html` is needed for the web version.  
  - The LaTeX/PDF output (`docs/latex`) is one-time and ignored in Git.

