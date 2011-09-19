from flask import Flask
from pyIvr.ext.flask.blueprintFlaskIvr import ivrBlueprint, ivrBlueprintUri

app = Flask(__name__)
app.register_blueprint(ivrBlueprint)

app.run(host='0.0.0.0', debug=True)
