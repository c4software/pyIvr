from flask import Flask
app = Flask(__name__)

from afIvr.guideVocal import guideVocal
from pyIvr.decorator import render
gv = guideVocal("guide.json")

@app.route("/")
@render('vxml','2.0')
def main():
  return [	
          {"type":"message", "parametre": {"ressource":gv.getElement("begin"),"idBlock":"message1","nextId":"#message2"}},
          {"type":"message", "parametre": {"ressource":gv.getElement("end"),"idBlock":"message2","nextId":"#end"}},
          {"type":"disconnect", "parametre": {"idBlock":"end"}},
         ]
	
app.run(host='0.0.0.0', debug=True)
