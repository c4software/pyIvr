import json

__version__ = "0.1dev"

class guideVocal: 

  #: Contient le contenu du guide.
  guide = {}
  
  #: Emplacement du "guide.json" sur le disque.
  empGuide = ""

  def __init__(self,empGuide="guide.json"):
    #: Emplacement du Guide
    self.empGuide = empGuide
    
    #: Si le chargement echoue on raise une exception.
    if not self.loadGuide():
      raise Exception("Erreur lors du chargement du guide")
    return None


  def loadGuide(self):
    """
      Permet de charger le guide vocal present dans empGuide.   
    """ 

    #: Parcours du fichier.
    with open(self.empGuide, 'r') as f:
        fileGuide = f.read()
    f.closed
  
    #: Tentative de chargement du Json contenu.
    try:
      self.guide = json.loads(fileGuide)
      #: Chargement OK.
      return True
    except:
      #: Chargement NOK
      return False


  def getElement(self, key):
    """Permet de retourner l'element a l'emplacement key dans la variable guide.
      :param key clef utiliser pour recuperer la valeur dans le guide Vocal.
    """
    try:
      return self.guide[key]
    except:
      return None
