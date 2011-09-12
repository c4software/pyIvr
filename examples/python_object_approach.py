from pyIvr.ext.afone.guideVocal import guideVocal
from pyIvr.base import renderBase

# CREATION DES OBJETS DE BASE
gv = guideVocal("guide.json")
b = renderBase(render='vxml',version='2.0')

# DEBUT CONSTRUCTION SVI
b.message({"ressource":gv.getElement("son1"),"idBlock":"message1","nextId":"#message2"})
b.message({"ressource":gv.getElement("son2"),"idBlock":"message2","nextId":"#end"})
b.disconnect({"idBlock":"#end"})

# AFFICHAGE DU RENDU FINAL
print b.final_render({"begin":"message1"})
