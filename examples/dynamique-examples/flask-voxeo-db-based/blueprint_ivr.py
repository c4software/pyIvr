from flask import Blueprint, session, redirect
from pyIvr import dynamiqueIvr
from pyIvr import render

ivrDemo = Blueprint('DynamiqueIvr', __name__)

@ivrDemo.route("/ivr/")
@ivrDemo.route("/ivr/<step>")
def ivr(step=None):
  if not 'ivr' in session:
    # Si aucun IVR charge alors on retourne au /
    return redirect('/')
  else:
    # Si un IVR est charge on essaye de l'afficher
    return makeResponse(step)

@render('vxml','2.0')
def makeResponse(step=None):
  # Creation d'une reponse.
  jsonLoader = dynamiqueIvr(stringJson=session['ivr'])
  if step is None:
    step = jsonLoader.getParams()['begin']
  return jsonLoader.getParamAndStep(step,True,'ivr/')


# Generation du SVI d'erreur
def get_error_svi():
  session['ivr'] = """{
  "params": {
    "begin": "errorMessage"
  },
  "svi":{
    "errorMessage": {
      "type": "message",
      "parametre": {
        "ressource": {
          "son": "/static/error.wav",
          "text": "Introuvable"
        },
        "idBlock": "errorMessage",
        "nextId": "end"
      }
    },
    "end": {
      "type": "disconnect",
      "parametre": {
        "idBlock": "end"
      }
    }
  }
}"""
