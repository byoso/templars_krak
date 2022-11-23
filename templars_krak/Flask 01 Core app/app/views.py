
from app import app


@app.route("/")
def index():
    return "<h1>Flask app is running</h1>"
