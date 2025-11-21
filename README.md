# QR-Code-Generator
# ⭐QR Code Generator Website (Python + Flask)

A simple, clean, and user-friendly web application built using Python, Flask, and qrcode library.
Users can enter any text or URL and instantly generate a downloadable QR code.
All QR code images are automatically saved inside a dedicated folder.

# 📁 Project Folder Structure

qr_website/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── qrcodes/
│        └── (Generated QR code images will be saved here)
│
└── README.md

# 🚀 Features

🔹 Generate QR code from any text or URL

🔹 Responsive layout (mobile + desktop)

🔹 Auto-generated unique filenames

🔹 Download button for QR code

🔹 “Generate Another QR” button

🔹 QR code auto-resizes based on screen size

🔹 All QR codes stored in a dedicated folder

🔹 Clean modern UI with custom CSS

# 🛠️ Technologies Used

Python 3

Flask

qrcode

Pillow (required by qrcode)

HTML5

CSS3

# 📦 Required Python Packages

Install all required packages using:

pip install flask qrcode pillow

# ▶️ How to Run the Project

Open terminal inside the project folder:

cd qr_website


Run the Flask application:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


You're ready to generate QR codes! 🎉
