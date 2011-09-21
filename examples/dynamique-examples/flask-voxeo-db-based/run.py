from flask import Flask, session, request

# Import de la session pour les requete SQL.
from database import db_session

# Declaration de l'application
app = Flask(__name__)
app.secret_key = 'li4Q~wNV7%RO?3=r.s|am^3>V:.cY22N%*>+%i=p/B6!1-HMv!/a8w@]Fk2n'

@app.route("/")
def hello():
    return session['calledid']

# Fonction appele a chaque appel HTTP
@app.before_request
def before_request():
    """
      Si un session.calledid est passe en parametre alors on le sauvegarde 
      pour pouvoir recuperer le SVI correspondant a au numero appele.
      
      Dans le cas de voxeo le session.calledid est passe en parametre GET
      lors du premier appel.
    """
    calledid = request.args.get('session.calledid','')
    if calledid is not "":
      session['calledid'] = calledid

# Permet de fermer la connexion mySQL.
@app.teardown_request
def shutdown_session(exception):
    db_session.remove()

app.run(debug=True)
