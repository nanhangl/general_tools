# the purpose of this script is to bulk resize image (aspect ratio maintained)

import glob, os
from PIL import Image

os.chdir("img_dir")
fileList = os.listdir()

for fileName in glob.glob("*.png"):
    image = Image.open(fileName)
    image.thumbnail((227, 227))
    image.save(fileName)
