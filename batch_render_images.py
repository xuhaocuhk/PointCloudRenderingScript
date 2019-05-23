import os

root = lux.getSceneTree()
for node in root.find( types = lux.NODE_TYPE_MODEL ):
	print(node.getName())
	node.hide()

for node in root.find(types = lux.NODE_TYPE_MODEL):
	node.show()
	lux.renderImage("./image_" + node.getName() + ".png", width = 2500, height = 2000)
	node.hide()
