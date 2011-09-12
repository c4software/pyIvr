from functools import wraps
from .base import renderBase

def render(render='vxml',version='2.0'):
  def decorator(fonction):
    @wraps(fonction)
    def decorated_function(*args, **kwargs):
        # Creation de l'objet qui permet de faire le rendu
        b = renderBase(render,version)

        # Recuperation des parametres et des blocks a inserer dans le rendu
        blockAndParam = fonction(*args, **kwargs)
        for key, elem in blockAndParam['svi'].iteritems():
          # On parcour les blocks pour creer le rendu
          if hasattr(b, elem['type']): 
              _member = getattr(b, elem['type']) # Recuperation de la methode dans renderBase
              _member(elem['parametre'])  # Appel de la methode avec les parametres.

        # On retourne le rendu final
        if render == 'vxml':
            return b.final_render(blockAndParam['params']), 200, {'Content-Type': 'text/xml'}
        else:
            return b.final_render(blockAndParam['params'])
    return decorated_function
  return decorator


def _render(blockAndParam={}, render="vxml", version="2.0"):
  # Creation de l'objet qui permet de faire le rendu
  b = renderBase(render,version)
  
  for key, elem in blockAndParam['svi'].iteritems():
    # On parcour les blocks pour creer le rendu
    if hasattr(b, elem['type']): 
        _member = getattr(b, elem['type'])
        _member(elem['parametre'])  

  # On retourne le rendu final
  if render == 'vxml':
      return b.final_render(blockAndParam['params']), 200, {'Content-Type': 'text/xml'}
  else:
      return b.final_render(blockAndParam['params'])
  
