class Mapmanager():
   """ Управление картой """
   def __init__(self):
       self.model = 'block' # модель кубика лежит в файле block.egg
       # # используются следующие текстуры:
       self.texture = 'block.png'         
       self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
       ] #rgba
       # создаём основной узел карты:
       self.startNew()
       # self.addBlock((0,10, 0))
 
   def startNew(self):
       """создаёт основу для новой карты"""
       self.land = render.attachNewNode("Land") # узел, к которому привязаны все блоки карты

 
   def addBlock(self, position):
       # создаём строительные блоки
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position)
       self.color = self.getColor(int(position[2]))
       self.block.setColor(self.color)
       self.block.reparentTo(self.land)
 

 
  