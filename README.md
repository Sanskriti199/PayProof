# PayProof – UPI Payment Verification System

## Project Overview
UPI payments are widely used in everyday transactions, but fake payment screenshots and risky payment attempts have become increasingly common. Many users rely on screenshots without having an easy way to verify whether a payment is genuine.

**PayProof** is a web‑based system designed to help users:
- Verify the authenticity of UPI payment screenshots
- Assess the risk level of a UPI payment using basic transaction details

The project focuses on building a practical and easy‑to‑use solution that improves awareness and helps reduce common UPI‑related scams.

## Key Features

### Screenshot Verification
- Users upload a UPI payment screenshot
- The system analyzes:
  - Image quality and blur
  - Text clarity using OCR
  - Presence of important transaction details
- Screenshots are classified as:
  - Genuine
  - Suspicious
  - Likely Fake
- A short explanation is provided for transparency

### Payment Risk Analysis
- Users enter basic payment details such as:
  - Amount
  - Time of payment
  - Whether the payer is new or unknown
- The system evaluates the information and assigns a risk level:
  - Safe
  - Medium Risk
  - High Risk
- Each result includes a clear reason for the assigned risk level

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

## Team and Contributions

This project was developed by a two‑member team .

### Sanskriti Mittal – Backend and AI/ML
- Image forensics and preprocessing using OpenCV  
- OCR‑based text extraction from UPI screenshots  
- Machine learning model for screenshot classification  
- Backend API development using Flask/FastAPI  
- Database handling and result storage  

### Manyata Sharma – Frontend and Integration
- Streamlit‑based user interface design  
- Screenshot upload and payment detail form handling  
- Payment risk analysis logic  
- Integration of frontend with backend APIs  
- Documentation and user flow design  

## System Workflow
1. User uploads a screenshot or enters payment details  
2. Frontend sends data to backend APIs  
3. Backend performs image analysis, OCR, and ML classification  
4. Results are returned to the frontend  
5. User receives verification status and risk level with explanation  

## Future Scope
- Expanding the dataset with more real‑world samples  
- Supporting additional UPI apps and layouts  
- Improving UI for mobile responsiveness  
- Enhancing fraud detection accuracy  

## Disclaimer
This project is developed for educational purposes and provides risk indications, not guaranteed fraud detection.
