from flask import Flask, render_template, request
import qrcode
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    text = request.form["qr_text"]

    random_number = random.randint(1000,9999)
    filename = f"qr_generated_{random_number}.png"

    # Create qrcodes folder inside static if not exists
    folder = os.path.join("static", "qrcodes")
    os.makedirs(folder, exist_ok=True)

    # Save inside static/qrcodes/
    path = os.path.join(folder, filename)


    img = qrcode.make(text)
    img.save(path)

    return render_template("index.html", qr_filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
