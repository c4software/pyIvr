from flask import Blueprint
from pyIvr import dynamiqueIvr
from pyIvr import render

ivr = Blueprint('ivr', __name__)
sviJSON = "svi.json"
jsonLoader = dynamiqueIvr(sviJSON)

@ivr.route("/ivr")
@ivr.route("/ivr/<step>")
@render('vxml','2.0')
def ivr(step=None):
  if step is None:
    step = jsonLoader.getParams()['begin']
  
  return jsonLoader.getParamAndStep(step)
