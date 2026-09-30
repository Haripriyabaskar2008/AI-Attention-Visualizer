# AI-Attention-Visualizer
AI Image Text Extractor

An AI-powered image text extraction application built with Python and Streamlit. The application uses Optical Character Recognition (OCR) to extract readable text from uploaded images and calculates an OCR confidence score based on the recognition confidence of the detected text.

Overview

The AI Image Text Extractor allows users to upload an image containing text and automatically convert the visual content into editable digital text.

The application uses Tesseract OCR through the pytesseract Python library to recognize text. Along with the extracted text, it calculates an average OCR confidence score to indicate how confidently the text was recognized.

Features
Upload images in PNG, JPG, and JPEG formats
Extract text from images using OCR
Display extracted text in an editable text area
Calculate OCR recognition confidence score
Display the score as a percentage
Provide feedback based on OCR confidence
Simple and user-friendly Streamlit interface
Supports local image processing
Technologies Used
Python
Streamlit
Pytesseract
Tesseract OCR
Pillow
Optical Character Recognition (OCR)
System Workflow
Image Upload
     ↓
Image Processing
     ↓
Tesseract OCR
     ↓
Text Extraction
     ↓
OCR Confidence Calculation
     ↓
Extracted Text + Confidence Score
How It Works
1. Image Upload

The user uploads an image containing readable text.

Supported formats:

PNG
JPG
JPEG
2. OCR Text Extraction

The uploaded image is processed using Tesseract OCR.

The detected text is extracted and displayed in the application.

3. Confidence Score

Tesseract provides confidence values for recognized words.

The application calculates the average confidence value of the detected text.

For example:

OCR Confidence Score: 91.42%

A higher score indicates that Tesseract recognized the visible text with higher confidence.

Example
Input

An image containing:

Artificial Intelligence is a branch of
computer science that focuses on creating
intelligent machines.
Output
Extracted Text:

Artificial Intelligence is a branch of
computer science that focuses on creating
intelligent machines.

Example confidence:

OCR Confidence Score

91.42%
Project Structure
AI-Attention-Visualizer/
│
├── app.py
├── attention.py
├── embedding.py
├── ocr.py
├── requirements.txt
└── venv/
File Description
File	Description
app.py	Main Streamlit application
attention.py	Attention-related implementation
embedding.py	Embedding-related implementation
ocr.py	OCR-related functionality
requirements.txt	Python dependencies
Requirements

The project requires:

streamlit
pytesseract
pillow

The project also requires the Tesseract OCR engine to be installed on the system.

Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_LINK
2. Open the Project
cd AI-Attention-Visualizer
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

Windows:

.\venv\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
streamlit run app.py

The application will open in the browser.

Usage
Launch the Streamlit application.
Upload an image containing text.
Click Extract Text.
View the extracted text.
View the OCR confidence score.
Use the extracted text for further processing or editing.
OCR Confidence

The score displayed by the application represents OCR recognition confidence, not the correctness of an answer.

The score is calculated from the confidence values returned by Tesseract for the detected text.

Applications

This project can be useful for:

Digitizing printed documents
Extracting text from photographs
Converting scanned content into editable text
Document processing
Educational applications
Basic OCR demonstrations
Text extraction workflows
Limitations
OCR accuracy depends on image quality.
Blurry or low-resolution images may produce incorrect text.
Handwritten text may not be recognized accurately.
Complex layouts may affect extraction quality.
OCR confidence does not guarantee that every extracted word is correct.
Future Enhancements

Possible improvements include:

Support for handwritten text recognition
Multiple language OCR
PDF text extraction
Image preprocessing
Automatic text correction
Download extracted text as a file
Advanced document layout detection
Cloud deployment
Conclusion

The AI Image Text Extractor demonstrates how OCR technology can convert text from images into editable digital content. By combining Tesseract OCR with Streamlit, the project provides a simple interface for image-based text extraction and confidence analysis.
LIVE DEMO:
https://ai-attention-visualizer-bxwjw7bmmgd5syuahgshzr.streamlit.app/
<img width="952" height="268" alt="Screenshot 2026-09-30 193143" src="https://github.com/user-attachments/assets/efe7637f-28d5-4f14-81ec-5937c15aa6d1" />
<img width="957" height="397" alt="Screenshot 2026-09-30 193126" src="https://github.com/user-attachments/assets/6d5367dc-bac0-45c2-af78-975094e118e4" />
<img width="950" height="316" alt="Screenshot 2026-09-30 193107" src="https://github.com/user-attachments/assets/372e6f9b-4eea-4402-98c8-12b15fa0d442" />
<img width="954" height="379" alt="Screenshot 2026-09-30 193046" src="https://github.com/user-attachments/assets/3e2ff92d-d925-4182-9f2a-5bbbf6c9c7b6" />



Author

Haripriya B

 BSC Computer Science with Artificial Intelligence

