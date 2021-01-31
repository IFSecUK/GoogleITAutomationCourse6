
#Project of Google IT automation with Python Course 6 Lab 1

import os
from PIL import Image
# Import of necessary modules


new_path = "/opt/new_icons/"
list_of_images = []
path = os.walk("./images")
#Store the parent directory, subdirectories and files in the variable path

for root, directories, files in path:
	for file in files:
		list_of_images.append(file)
# We just need files and then storing them in the list.

for image in list_of_images:
	try:
		with Image.open("./images/" + image).convert("RGB") as im:
			path2, filename = os.path.split(image)
			#Split the path of the file  and the filename and store in the variables.
			filename = os.path.splitext(filename)[0]
			#Just store the filename excluding the extension
			im.resize((128,128)).rotate(270).save(f"{new_path}{filename}.jpeg")
			#Resize, rotate and save the new image in the required directory.
	except OSError:
		pass
		#IF any OSError exception just ignore the file and move on with the next file.



