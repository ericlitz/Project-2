from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/election_data.db.sqlite"

db = SQLAlchemy(app)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

# create flask route to access DB to convert sqlite to json

if __name__ == "__main__":
    app.run(debug=True)
