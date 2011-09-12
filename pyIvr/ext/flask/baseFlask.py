from pyIvr.decorator import render, _render
from flask.views import View

__version__ = "0.1dev"

class baseFlask(View):
  dynamiqueIvr = None
  langage = "vxml"
  version = "2.0"
  path = "/"
  
  def __init__(self, dynamiqueIvr=None, sviJSON="svi.json",langage="vxml",version="2.0",path="/"):
    """ Init de la classe de baseFlask.
        Cette class permet de gerer les url pour acceder a un SVI
        dynamique.
        
        Si dynamiqueIvr n'est pas passer en parametre il est cree 
        automatiquement et charge le fichier json specifier.
        
        :param dynamiqueIvr, objet dynamiqueIvr permetant le chargement 
        et parsage du json pour le svi.
        :param sviJSON, fichier json a charger par l'instance de dynamique
        Ivr
    """
    if dynamiqueIvr is None:
      from pyIvr.dynamiqueIvr import dynamiqueIvr
      self.dynamiqueIvr = dynamiqueIvr(sviJSON)
    else:
      self.dynamiqueIvr = dynamiqueIvr

    self.langage = langage
    self.version = version
    self.path    = path
  
  def dispatch_request(self,step=None):
      if step is None:
        step = self.dynamiqueIvr.getParams()['begin']
      return _render({"params":{"begin":step},"svi":self.dynamiqueIvr.getStep(step,True,self.path)},self.langage,self.version)
