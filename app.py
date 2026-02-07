from flask import Flask, render_template, request
from tasks import process_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filename = file.filename

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    process_file.delay(filename)

    return render_template("index.html",
                       message="✅ File uploaded successfully! Processing in background...")


if __name__ == "__main__":
    app.run(debug=True)
