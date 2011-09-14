from flask import Flask
app = Flask(__name__)

from pyIvr.ext.afone.guideVocal import guideVocal
from pyIvr import render
gv = guideVocal("guide.json")

@app.route("/")
@render('vxml','2.0')
def main():
  return {
    "params":{
      "begin":"message1"
    },
    "svi":{
	    "message1":{"type":"message", "parametre":   {"dynamique":"#", "ressource":gv.getElement("son1"),"idBlock":"message1","nextId":"message2"}},
	    "message2":{"type":"message", "parametre":   {"dynamique":"#", "ressource":gv.getElement("son2"),"idBlock":"message2","nextId":"end"}},
	    "end":{"type":"disconnect", "parametre": {"idBlock":"end"}}
    }
  }

app.run(host='0.0.0.0', debug=True)
