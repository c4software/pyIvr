from jinja2 import Environment, ChoiceLoader, FileSystemLoader
import os
#from jinja2 import PackageLoader

__version__ = "0.1dev"

class renderBase:

  render = ""
  version = ""
  content = ""

  def __init__(self,render="vxml",version="2.0"):
    """Initialisation de la class base.
      :param render, methode de rendu pour le client finale (vxml, html, xhtml, etc..)
      :param version, version pour le rendu (2.1, 2.2, 3.0, html5, etc...)
    """
    self.render = render
    self.version = version
    return None

  def __getattr__(self, attr):
    """
      Methode generique permetant au developpeur de definir n'importe
      quel template. Exemple :
        a = renderBase()
        a.demo()
        a.sommaire()
        ...
    """
    def default_method(*args):
      try:
        arrParam = args[0]
      except:
        arrParam = {}
        
      self.content = "".join([self.content, self.render_template(attr,**arrParam)])
    return default_method

  def render_template(self,templateUri, **context):
    #env = Environment(loader=PackageLoader('template', self.render+"/"+self.version))
    emplacement = os.path.dirname(__file__)
    env = Environment(loader=ChoiceLoader([
                                          FileSystemLoader(emplacement+'/templates/'+self.render+"/"+self.version),
                                          FileSystemLoader('templates/'+self.render+"/"+self.version)
                                          ]))
                                          
    template = env.get_template(templateUri)
    return template.render(context)
  
  def final_render(self,arrParam={}):
    return self.render_template('layout',content=self.content, **arrParam)

  #def message(self,arrParam={}):
  #  self.content = "".join([self.content, self.render_template('message',**arrParam)])

  #def sommaire(self,arrParam={}):
  #  self.content = "".join([self.content, self.render_template('sommaire',**arrParam)])

  #def disconnect(self,arrParam={}): 
  #  self.content = "".join([self.content, self.render_template('disconnect',**arrParam)])
