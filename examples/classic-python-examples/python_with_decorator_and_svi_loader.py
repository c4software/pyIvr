from pyIvr import dynamiqueIvr
from pyIvr import render

svi = dynamiqueIvr("svi.json")

# Fonction de test
@render()
def test():
  return svi.get()


print test()[0]
