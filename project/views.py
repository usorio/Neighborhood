from project import app

@app.route("/")
def hello():
    return "Nieghborhood"
