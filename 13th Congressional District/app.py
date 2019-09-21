from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/election_data.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

# create flask route to access DB to convert sqlite to json
@app.route("/election")
def ill_election_data():
    results = db.session.query(election_results_table.Precinct, election_results_table.Candidate_R,
        election_results_table.Percentage_R).all()
    df = pd.DataFrame(results, columns=['precinct', 'candidate', 'percent'])
    return df

if __name__ == "__main__":
    app.run(debug=True)
