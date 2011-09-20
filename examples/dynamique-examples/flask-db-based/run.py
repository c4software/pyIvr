from flask import Flask

# Import de la session pour les requete SQL.
from database import db_session

app = Flask(__name__)
app.secret_key = 'li4Q~wNV7%RO?3=r.s|am^3>V:.cY22N%*>+%i=p/B6!1-HMv!/a8w@]Fk2n'

# Declaration de l'application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Permet de fermer la connexion mySQL.
@app.teardown_request
def shutdown_session(exception):
    db_session.remove()

app.run(debug=True)
