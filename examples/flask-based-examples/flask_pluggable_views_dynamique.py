from flask import Flask
from pyIvr.ext.flask.baseFlask import baseFlask
from pyIvr import render
from pyIvr import dynamiqueIvr

app = Flask(__name__)


# Rules pour le routage des url.
app.add_url_rule("/svi/<step>", view_func=baseFlask.as_view("svi",langage="vxml",version="2.0",path="svi/"))
app.add_url_rule("/svi/", view_func=baseFlask.as_view("svi",langage="vxml",version="2.0",path="svi/"))

app.add_url_rule("/web/<step>", view_func=baseFlask.as_view("web",langage="xhtml",version="1.0",path="web/"))
app.add_url_rule("/web/", view_func=baseFlask.as_view("web",langage="xhtml",version="1.0",path="web/"))


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
