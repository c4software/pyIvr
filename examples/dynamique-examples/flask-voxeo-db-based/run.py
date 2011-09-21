from flask import Flask, session, request, redirect

# Import de la session pour les requete SQL.
from database import db_session

# Import des models
from models import Demo

# Import des blueprint
from blueprint_ivr import ivrDemo

# Declaration de l'application
app = Flask(__name__)
app.secret_key = 'li4Q~wNV7%RO?3=r.s|am^3>V:.cY22N%*>+%i=p/B6!1-HMv!/a8w@]Fk2n'

# Register des bluesprint
app.register_blueprint(ivrDemo)

@app.route("/")
def hello():
  if 'calledid' in session:
    return redirect('/ivr/')
  else:
    return "Aucun SVI en Session. Pour pouvoir continuer vous devez en charer un. Exemple : <a href='/?session.calledid=9996141833'>?session.calledid=9996141833</a>"
  
@app.route("/addElem")
def addElem():
  demoElem = Demo("9996141833",'{"params":{"begin":"sommaire1"},"svi":{"sommaire1":{"type":"sommaire","parametre":{"dynamique":"#","choices":[{"dtmf":"1","nextId":"message1"},{"dtmf":"2","nextId":"message2"}],"ressource":{"son":"/static/sommaire.wav","text":"Pour le choix ..."},"idBlock":"sommaire1"}},"message1":{"type":"message","parametre":{"dynamique":"#","ressource":{"son":"/static/son1.wav","text":"Bonjour ..."},"idBlock":"message1","nextId":"message2"}},"message2":{"type":"message","parametre":{"dynamique":"#","ressource":{"son":"/static/son2.wav","text":"Pour le choix ..."},"idBlock":"message2","nextId":"end"}},"pi":{"type":"pi","parametre":{}},"end":{"type":"disconnect","parametre":{"idBlock":"end"}}}}')
  db_session.add(demoElem)
  db_session.commit()
  return "Ajoute"

@app.route('/favicon.ico')
def empty():
  return ""

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
      session['ivr'] = Demo.query.filter(Demo.number == calledid).first().value

# Permet de fermer la connexion mySQL.
@app.teardown_request
def shutdown_session(exception):
    db_session.remove()

app.run(debug=True)
