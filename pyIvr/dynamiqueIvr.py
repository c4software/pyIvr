import json

__version__ = "0.1dev"

class dynamiqueIvr: 
  #: Contient le contenu du SVI.
  svi = {}
  
  #: Emplacement du JSON du SVI.
  empSVI = ""
  
  #: Nombre d'element dans le SVI.
  nbStep = 0
  
  def __init__(self,empSVI="svi.json",stringJson=None):
    #: Emplacement du SVI
    self.empSVI = empSVI

    if stringJson is not None:
      #: Chargement du json depuis une string.
      if not self.loadSVIString(stringJson):
        raise Exception("Erreur lors du chargement du SVI")
    else:
      #: Si le chargement echoue on raise une exception.
      if not self.loadSVI():
        raise Exception("Erreur lors du chargement du SVI")
    
    return None
  
  def loadSVIString(self,stringJson):
    """
      Charge le SVI depuis une string.
    """
    try:
      self.svi = json.loads(stringJson)
      self.nbElem = len(self.svi)-1
      return True
    except:
      return False
  
  def loadSVI(self):
    """
      Permet de charger le SVI present dans empSVI   
    """ 
    #: Parcours du fichier.
    with open(self.empSVI, 'r') as f:
        fileSVI = f.read()
    f.closed
    #: Tentative de chargement du Json contenu.
    try:
      self.svi = json.loads(fileSVI)
      self.nbElem = len(self.svi)-1
      #: Chargement OK.
      return True
    except:
      #: Chargement NOK
      return False
  
  def get(self):
    """
      Permet de retourner l'integraliter du JSON.
    """
    return self.svi
  
  def getStep(self, step=None, dynamique=False,subFolder=None):
    """
      Permet de retourner une etape specifique du JSON.
      :param step intituler de l'etape a recuperer.
      :param dynamique indique si le rendu est en mode dynamique dans la 
      liste des parametres de celui-ci.
      :param subFolder permet de specifier un dossier specifique lors 
      de la generation de l'url.
    """
    try:
      if not dynamique:
        self.svi['svi'][step]['parametre']["dynamique"] = "#"
      else:
        if subFolder is not None:
          self.svi['svi'][step]['parametre']["dynamique"] = "/"+subFolder
        else:
          self.svi['svi'][step]['parametre']["dynamique"] = "/"
        
      return {step:self.svi['svi'][step]}
    except: 
      return {}
    
  def getParams(self):
    """
      Retourne les parametres du SVI
    """
    try:
      return self.svi['params']
    except: 
      return {}

  def getParamAndStep(self, step=None, dynamique=False,subFolder=None):
    """
      Permet de recuperer une etape ainsi que les parametre
      specifique du JSON
    """
    return {"params":self.getParams(),"svi":self.getStep(step,dynamique,subFolder)}
