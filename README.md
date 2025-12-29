# PayProof – UPI Payment Verification System

## Project Overview
UPI payments are widely used, but fake payment screenshots and risky transactions are a common issue. Many users rely on screenshots without being able to verify whether a payment is genuine.

**PayProof** is a web‑based system that helps users:
- Verify the authenticity of UPI payment screenshots
- Assess the risk level of a UPI payment using basic transaction details

The project focuses on a practical, easy‑to‑use solution for improving UPI payment safety.

## Key Features
- Screenshot authenticity check (Genuine / Suspicious / Likely Fake)
- OCR‑based text extraction and image quality analysis
- Payment risk analysis (Safe / Medium Risk / High Risk)
- Clear, explainable results for users

## Tech Stack

### Backend and AI/ML
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=flat&logo=opencv&logoColor=white)
![Tesseract OCR](https://img.shields.io/badge/Tesseract%20OCR-5A5A5A?style=flat)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

### Development Tools
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)

## User Flow
1. User uploads screenshot
2. User enters payment details
3. Clicks Check Payment
4. Sees risk result + explanation

## How It Works
1. User uploads a UPI screenshot or enters payment details  
2. Frontend sends data to backend APIs  
3. Backend performs OCR, image analysis, and ML‑based classification  
4. Verification result and risk level are returned and displayed  

## Team Contributions
- **Sanskriti Mittal:** Backend development, image processing, OCR integration, ML model training  
- **Manyata Sharma:** Frontend development, API integration, risk analysis logic, documentation  

## Future Scope
- Expanding the dataset with more real‑world samples  
- Supporting additional UPI apps and layouts  

## Disclaimer
This project is developed for educational purposes and provides risk indications, not guaranteed fraud detection.
