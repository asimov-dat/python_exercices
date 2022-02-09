import sys
import os
from PIL import Image

taget = '.png'

# grab arguments
origin_dir = str(sys.argv[1])
destin_dir = str(sys.argv[2])

# check if folder exist if not create it

if exists := os.path.exists(f'./{destin_dir}'):
    path = f'/home/dat/code/python/python_exercices/apps/images/{destin_dir}'
else:
    os.mkdir(f'./{destin_dir}')
    path = f'/home/dat/code/python/python_exercices/apps/images/{destin_dir}'

# loop 
images = os.scandir(f'./{origin_dir}') 

for image in images:
    img_path = image.path
    img_name = image.name.rstrip('.jpg')
    temp = Image.open(img_path)
    temp.save(path+img_name+taget,'png')

images.close()    

    


# conver

# save