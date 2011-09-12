from pyIvr.dynamiqueIvr import dynamiqueIvr
from pyIvr.decorator import render

svi = dynamiqueIvr("svi.json")

# Fonction de test
@render()
def test():
  return svi.get()


print test()[0]
