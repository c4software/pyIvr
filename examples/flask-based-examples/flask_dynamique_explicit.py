from flask import Flask

from pyIvr import render
from pyIvr import dynamiqueIvr
svi = dynamiqueIvr("svi.json")

from pyIvr.ext.flask.baseFlask import baseFlask

app = Flask(__name__)

@app.route("/web/<step>")
@app.route("/web/")
@render('xhtml','1.0')
def stepByStepWebSvi(step=None):
  if step is None:
    step = svi.getParams()['begin']
  return {"params":{"begin":step},"svi":svi.getStep(step,True,"web/")}

@app.route("/svi/<step>")
@app.route("/svi/")
@render('vxml','2.0')
def stepByStepSvi(step=None):
  if step is None:
    step = svi.getParams()['begin']
  return {"params":{"begin":step},"svi":svi.getStep(step,True,"svi/")}

@app.route("/full/")
@render('vxml','2.0')
def fullSvi():
  svi = dynamiqueIvr("svi.json")
  return svi.get()

@app.route("/")
def main():
  return """
          <ul>
            <li><a href="/web/">WebSvi</a></li>
            <li><a href="/svi/">Svi etape par etape</a></li>
            <li><a href="/full/">Full SVI</a></li>
          </ul>
         """

@app.route("/favicon.ico")
def fakeFavicon():
  return ""
	
app.run(host='0.0.0.0', debug=True)
