from flask import Blueprint, render_template, redirect, url_for, request
from models import Demo
from database import db_session

ivrIhmDemo = Blueprint('DynamiqueIvrIhm', __name__)

@ivrIhmDemo.route('/')
def index():
  demos = Demo.query.all()
  return render_template('listing.html',demos=demos)
  
@ivrIhmDemo.route('/newApplication')
def newApplication():
  actionUrl = url_for('DynamiqueIvrIhm.saveApplication')
  return render_template('formulaire.html',action="Ajouter", actionUrl=actionUrl)

@ivrIhmDemo.route('/loadApplication/<demo_id>')
def loadApplication(demo_id=None):
  actionUrl = url_for('DynamiqueIvrIhm.saveApplication')
  laDemo = Demo.query.filter(Demo.id == demo_id).first()
  return render_template('formulaire.html',action="Modifier", actionUrl=actionUrl,value=laDemo.value,number=laDemo.number,id=laDemo.id)

@ivrIhmDemo.route('/saveApplication', methods=['POST'])
def saveApplication():
  id = request.form['id']
  number = request.form['number']
  value = request.form['value']
  
  if id == "":
    maDemo = Demo(number=number,value=value)
    db_session.add(maDemo)
    db_session.commit()
  else:
    db_session.query(Demo).filter_by(id=id).update({"number": number,"value": value})
  
  db_session.commit()
  return redirect(url_for('DynamiqueIvrIhm.index'))
