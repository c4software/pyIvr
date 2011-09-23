from flask import Blueprint
from pyIvr import dynamiqueIvr
from pyIvr import render

ivrBlueprint = Blueprint('ivr', __name__)
jsonLoader = dynamiqueIvr("svi.json")

@ivrBlueprint.route("/ivr/")
@ivrBlueprint.route("/ivr/<step>")
@render('vxml','2.0')
def ivr(step=None):
  if step is None:
    step = jsonLoader.getParams()['begin']
  
  return jsonLoader.getParamAndStep(step,True,'ivr/')
