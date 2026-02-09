# PDF Editor Pro

A Flask-based web application for performing common PDF operations through a clean, modular backend architecture.

This project converts a command-line PDF utility into a scalable and maintainable web application.

---

## Features

- Convert PDF to Word
- Extract selected pages from PDF
- Merge multiple PDF files
- Encrypt PDF with password protection
- Rotate PDF pages
- Delete specific pages from PDF
- Convert PDF pages to images
- Compress PDF files

---

## Tech Stack

- **Backend:** Python, Flask  
- **PDF Processing:** PyPDF2, pikepdf, pdf2docx, pdf2image  
- **Image Handling:** Pillow  
- **Frontend:** HTML, CSS (basic templates)

---

## Project Structure

```

pdf-editor-pro/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── templates/
│   └── static/
│
├── uploads/
├── outputs/
├── tests/
│
├── config.py
├── run.py
├── requirements.txt
└── README.md

````

---

## How to Run Locally

1. Clone the repository  
   ```bash
   git clone <your-repo-url>
   cd pdf-editor-pro
````

2. Create virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
````

3. Install dependencies
   ```bash
   pip install -r requirements.txt
````

4. Run the Flask application
   ```bash
   python run.py
````

5. Open browser and visit
   ```
   http://127.0.0.1:5000/
````

---

## Design Approach

* Business logic separated from routes
* Service-based architecture for scalability
* File handling isolated in utility modules
* Easy to extend with new PDF features

---

## Future Improvements

* User authentication
* Drag-and-drop UI
* Cloud storage integration
* Background task processing

---

## Author

Developed as a learning-focused backend project to demonstrate clean architecture, modular design, and real-world PDF processing.
