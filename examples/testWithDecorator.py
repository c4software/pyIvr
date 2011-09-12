from afIvr.guideVocal import guideVocal
from pyIvr.decorator import render

gv = guideVocal("guide.json")

# Fonction de test
@render()
def test():
  return [	
  			{"type":"message", "parametre": {"ressource":gv.getElement("begin"),"idBlock":"message1","nextId":"#message2"}},
			{"type":"message", "parametre": {"ressource":gv.getElement("end"),"idBlock":"message2","nextId":"#end"}},
  			{"type":"disconnect", "parametre": {"idBlock":"end"}},
         ]


print test()
