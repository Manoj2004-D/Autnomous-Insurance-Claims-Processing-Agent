# Autonomous Insurance Claims Processing Agent

An AI-powered Insurance Claims Processing System that automates the initial stage of insurance claim handling by extracting information from FNOL(First Notice of Loss) documents, validating mandatory fields, applying business routing rules, and returning a structured JSON response.

---

## Project Objective

The objective of this project is to automate the first stage of insurance claim processing.

The system:

* Accepts FNOL documents in **PDF** or **TXT** format.
* Extracts key claim information using **Google Gemini AI**.
* Detects missing mandatory fields.
* Applies predefined business routing rules.
* Generates a reasoning for the routing decision.
* Returns the final result in JSON format.
* Provides a user-friendly web interface built with HTML, CSS, and JavaScript.

---

# Features

* Upload PDF/TXT FNOL documents
* Automatic text extraction
* AI-powered field extraction using Gemini
* Missing field detection
* Rule-based claim routing
* Reason generation
* JSON output
* Modern responsive UI
* FastAPI backend

---

# 🛠 Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* FastAPI
* Python

## AI

* Google Gemini API

## Libraries

* PyMuPDF
* Pydantic
* python-dotenv
* Jinja2
* python-multipart

---

# Project Structure

```text
InsuranceClaimAgent/

│── app.py
│── requirements.txt
│── .env

├── templates/
│     index.html

├── static/
│     style.css
│     script.js

├── services/
│     pdf_reader.py
│     extractor.py
│     validator.py
│     router.py

├── models/
│     schemas.py

├── prompts/
│     extraction_prompt.txt

├── outputs/

└── data/
```

---

# Workflow

```text
User Uploads PDF/TXT
          │
          ▼
Frontend (HTML/CSS/JS)
          │
          ▼
FastAPI Backend
          │
          ▼
Extract Text (PyMuPDF)
          │
          ▼
Gemini AI
          │
          ▼
Extract Structured Fields
          │
          ▼
Validate Mandatory Fields
          │
          ▼
Apply Routing Rules
          │
          ▼
Generate JSON Response
          │
          ▼
Display Results on UI
```

---

# Extracted Fields

The AI extracts:

### Policy Information

* Policy Number
* Policyholder Name
* Effective Dates

### Incident Information

* Incident Date
* Incident Time
* Location
* Description

### Involved Parties

* Claimant
* Third Parties
* Contact Details

### Asset Details

* Asset Type
* Asset ID
* Estimated Damage

### Other Fields

* Claim Type
* Attachments
* Initial Estimate

---

# Business Rules

| Rule                                               | Recommended Route   |
| -------------------------------------------------- | ------------------- |
| Estimated Damage < ₹25,000                         | Fast-track          |
| Missing Mandatory Fields                           | Manual Review       |
| Description contains fraud / staged / inconsistent | Investigation Flag  |
| Claim Type = Injury                                | Specialist Queue    |
| Otherwise                                          | Standard Processing |

---

# JSON Output

```json
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
```

---

# Steps to Run

## 1. Clone the repository

```bash
git clone https://github.com/Manoj2004-D/Autnomous-Claims-Processing-Agent.git
```

## 2. Navigate to the project

```bash
cd InsuranceClaimAgent
```

## 3. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file.

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 6. Run the application

```bash
uvicorn app:app --reload
```

---

## 7. Open the browser

```
http://127.0.0.1:8000
```

---

## 8. Upload an FNOL PDF/TXT

Click **Choose File**, select a document, and click **Process Claim**.

The application will display:

* Extracted Fields
* Missing Fields
* Recommended Route
* Reason

---

# Sample Output

```json
{
  "extractedFields": {
    "policyNumber": "VH12345678",
    "policyholderName": "John Doe",
    "estimatedDamage": 18000,
    "claimType": "Vehicle"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below ₹25,000."
}
```

---

# Future Enhancements

* OCR support for scanned PDFs
* SQLite/PostgreSQL claim history
* User authentication
* Drag-and-drop upload
* Dashboard with analytics
* Email notifications
* Cloud deployment
* Docker support

---

# Author

**Manoj D**

