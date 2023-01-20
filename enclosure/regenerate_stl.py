import FreeCAD as App
import Mesh

doc = App.openDocument('protector.FCStd')

__objs__ = []
__objs__.append(doc.getObject("Body")) 
Mesh.export(__objs__, 'protector.stl')
del __objs__

App.closeDocument(doc.Label)

doc = App.openDocument('frontpanel.FCStd')

__objs__ = []
__objs__.append(doc.getObject("Body")) 
Mesh.export(__objs__, 'frontpanel.stl')
del __objs__

App.closeDocument(doc.Label)
