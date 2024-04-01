from PIL import Image
import os

for file in os.listdir('orig'):
	if file.endswith('.jpg'):
		image_file = Image.open('orig/' + file) # open colour image
		image_file = image_file.convert('L') # convert image to black and white
		image_file.save('result/' + file[:-4] + '_grey.png')