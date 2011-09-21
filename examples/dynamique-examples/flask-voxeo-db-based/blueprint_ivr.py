from flask import Blueprint, session
from pyIvr import dynamiqueIvr
from pyIvr import render

ivrDemo = Blueprint('DynamiqueIvr', __name__)

@ivrDemo.route("/ivr/")
@ivrDemo.route("/ivr/<step>")
@render('vxml','2.0')
def ivr(step=None):
  jsonLoader = dynamiqueIvr(stringJson=session['ivr'])
  print jsonLoader.svi['params']
  if step is None:
    step = jsonLoader.getParams()['begin']
  
  return jsonLoader.getParamAndStep(step)
