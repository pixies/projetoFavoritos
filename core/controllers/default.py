from core import app

@app.route("/")
def index():
    return "ola mundo"

