# 🌞 Solar Industry AI Assistant

An AI-powered tool to analyze rooftop images and assess solar panel installation potential using FastAPI.

---

## 📌 Features

- Upload satellite rooftop images (JPEG/PNG)
- Analyze sunlight exposure using basic brightness logic
- Get solar potential rating & ROI estimate
- JSON-based API response

---
## 🧠 Implementation Overview

- **Framework:** FastAPI
- **Method:** Basic brightness detection logic on satellite images
- **Function:** `analyze_rooftop_image()` processes uploaded image and estimates:
  - Rooftop suitability
  - Potential ROI

## 🚀 Setup Guide (Local)

### 1. Clone or Unzip the Project

git clone <https://github.com/yashpatilthethinker/solar_ai_assistant>
# OR if using the zip:
unzip solar_ai_assistant.zip
cd solar_ai_assistant

python -m venv venv
venv\Scripts\activate  

pip install -r requirements.txt

uvicorn app.main:app --reload

solar_ai_assistant/
├── app/
│   ├── main.py
│   └── utils.py
├── requirements.txt
├── README.md

## 📊 Example Analysis

**Sample Upload:** rooftop_sample.jpg  
**API Response:**
```json
{
  "status": "success",
  "message": "Test analysis completed successfully.",
  "solar_potential": "High",
  "roi_years": 4.2
}
}

---

For queries, reach out to: [Name : Yash Patil / Email: yashpatil7157@gmail.com]



