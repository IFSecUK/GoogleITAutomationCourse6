
#Project of Google IT automation with Python Course 6 Lab 1

import os
from PIL import Image

new_path = "/opt/new_icons/"
list_of_images = []
path = os.walk("./images")


for root, directories, files in path:
	for file in files:
		list_of_images.append(file)

for image in list_of_images:
	try:
		with Image.open("./images/" + image).convert("RGB") as im:
			path2, filename = os.path.split(image)
			filename = os.path.splitext(filename)[0]
			im.resize((128,128)).rotate(270).save(f"{new_path}{filename}.jpeg")
	except OSError:
		pass


