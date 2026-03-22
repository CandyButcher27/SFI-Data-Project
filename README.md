# SFI Data Information Extractor

An LLM-powered document intelligence pipeline built during an internship at SFI Data. The system processes corporate financial PDFs — Second Party Opinion (SPO) reports, sustainability frameworks, and term sheets — and outputs structured, analysis-ready Excel files.

---

## Problem Context

Financial analysts at SFI Data spent significant manual effort reading dense, inconsistently formatted corporate PDFs to extract a standard set of data fields. The documents were long (50–200+ pages), varied in layout, and contained both free-form narrative and embedded tables — neither of which existing PDF parsers handled well together.

This pipeline automates both extraction pathways and reduces document processing to a single command.

---

## System Architecture

The pipeline is split into two parallel tracks depending on data type:

### Track 1 — Textual Data Pipeline

```
PDF(s)
  │
  ▼
extractor.py       ← PyPDF2-based text extraction per page
  │
  ▼
parser.py          ← Chunks text → builds vector DB → retrieves relevant chunks
  │                   per field → queries LLM with structured JSON prompt
  ▼
writer.py          ← Parses LLM JSON output → writes to Excel via openpyxl
  │
  ▼
output.xlsx
```

### Track 2 — Tabular Data Pipeline

```
PDF(s)
  │
  ▼
table_extractor.py  ← LLMWhisperer API extracts tables with layout preservation
  │
  ▼
table_parser.py     ← Full table passed as context (no chunking — avoids
  │                    row/column boundary loss) → LLM extracts structured data
  ▼
table_writer.py     ← Writes structured output to Excel
  │
  ▼
output.xlsx
```

**Why different chunking strategies for text vs. tables?**
Text fields are long and diffuse — chunking + vector retrieval focuses the LLM on the relevant passage without exceeding context limits. Tables are short but spatially structured: chunking destroys row-column relationships. For tables, the entire extracted content is passed as a single context block.

---

## LLM Integration

Prompts are stored as structured JSON files in `Prompts/`, not hardcoded. This decouples field definitions from pipeline logic, making it straightforward to add new extraction targets without modifying code.

The system is provider-agnostic by design — it supports OpenAI, Gemini, and Groq interchangeably. This was intentional: different document types performed differently across providers during testing, and the internship scope required flexibility to swap without refactoring.

Prompts instruct the model to return only valid JSON with no preamble, which is then parsed and validated before writing to Excel. Malformed responses are caught and logged rather than silently written.

---

## Document Types Supported

| Type | Input | Prompt File |
|---|---|---|
| SPO + Framework | Two PDFs per company subfolder | `Prompts/prompts_spo_framework.json` |
| Term Sheets | One PDF per entry | `Prompts/prompts_term_sheet/` |

---

## Setup

```bash
git clone https://github.com/CandyButcher27/SFI-Data-Project.git
cd SFI-Data-Project
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set API keys:
```bash
export LLMWHISPERER_API_KEY='...'
export OPENAI_API_KEY='...'       # or GEMINI_API_KEY / GROQ_API_KEY
```

Run:
```bash
# SPO + Framework pipeline
cd Python_spo_framework && python main.py

# Term Sheet pipeline
cd Python_term_sheet && python main.py
```

Output: structured `.xlsx` files with one row per company/document.

---

## Configuration Notes

- LLMWhisperer endpoint is region-configurable (US: `us-central`, EU: `eu-west`)
- Each company's documents go in a subfolder under `Main_spo_framework/` — framework PDF first, SPO PDF second
- Prompts are the primary configuration surface — no code changes needed to add new fields

---

## Documentation

Full API documentation generated with Doxygen. View locally:

```
docs/html - Python_spo_framework/index.html
docs/html - Python_term_sheet/index.html
```

Regenerate:
```bash
cd Python_spo_framework && doxygen Doxyfile
```

---

## Project Structure

```
SFI-Data-Project/
├── Python_spo_framework/    # Textual + tabular pipeline for SPO/framework docs
├── Python_term_sheet/       # Pipeline variant for term sheets
├── Main_spo_framework/      # Input PDFs (per-company subfolders)
├── Main_term_sheet/         # Input PDFs for term sheets
├── Prompts/                 # JSON prompt definitions (field extraction targets)
└── requirements.txt
```

---

## Built During

Internship at **SFI Data**
