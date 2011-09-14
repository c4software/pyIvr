from flask import Flask
from pyIvr.ext.flask.baseFlask import baseFlask
from pyIvr.decorator import render
from pyIvr.dynamiqueIvr import dynamiqueIvr

app = Flask(__name__)

blog = dynamiqueIvr("blog.json")

@app.route("/")
@app.route("/<step>")
@render('xhtml','1.0')
def home(step=None):
  if step is None:
    return blog.get()
  else:
    return blog.getParamAndStep(step)
	
app.run(host='0.0.0.0', debug=True)
