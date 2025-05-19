from flask import Flask, render_template, redirect, url_for
import os
from crawler import run_crawler

app = Flask(__name__)

@app.route("/")
def index():
    image_dir = "static/captures"
    images = sorted(os.listdir(image_dir)) if os.path.exists(image_dir) else []
    return render_template("index.html", images=images)

@app.route("/run")
def run():
    run_crawler()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
