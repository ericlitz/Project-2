import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///projectDB.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
election_results = Base.classes.Election_Data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/election<br/>"
    )


@app.route("/election")
def full_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all election data
    results = session.query(election_results).all()

    session.close()

    # Convert list of tuples into normal list
    all_election_data = list(np.ravel(results))

    return jsonify(all_election_data)

@app.route("/election_results")
def election_res():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(election_results.Precinct, election_results.Candidate_R, election_results.Percentage_R, election_results.Raw_Vote_R, election_results.Candidate_D, election_results.Percentage_D, election_results.Raw_Vote_D).all()
    
    session.close()
    # Create a dictionary from the row data and append to a list of all_election_data
    election_data = []
    for Precinct, Candidate_R, Percentage_R, Raw_Vote_R, Candidate_D, Percentage_D, Raw_Vote_D  in results:
        election_dict = {}
        election_dict["Precinct"] = Precinct
        election_dict["Candidate_R"] = Candidate_R
        election_dict["Percentage_R"] = Percentage_R
        election_dict["Raw_Vote_R"] = Raw_Vote_R
        election_dict["Candidate_D"] = Candidate_D
        election_dict["Percentage_D"] = Percentage_D
        election_dict["Raw_Vote_D"] = Raw_Vote_D
        election_data.append(election_dict)

        return jsonify(election_data)


if __name__ == '__main__':
    app.run(debug=True)
