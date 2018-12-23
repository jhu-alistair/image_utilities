'''
This script walks through the specified directory, identifies tiff or jpeg image files and
creates a yaml side-car medatada file for unique each base name. If you have a tiff
and a jpeg with the same name you get only one yaml file. The script populates the image file
name and the image file creation date. The rest of the yaml file is hard coded in this script
'''

import os
from pathlib import Path
import imghdr

valid_image_types = ['tiff', 'jpeg']

# Set the folder path
folderpath = Path.home()  / 'Desktop/_Alistair/photos/scans'

# Iterator that returns the base names of image files a directory
def image_base_names(path):
    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        if os.path.isfile(img_path):
            if (imghdr.what(img_path) in valid_image_types):
                yield os.path.splitext(img)[0]

# Create a set of the unique base names of the image files in the spcified directory
image_set = set()
if (Path.exists(folderpath)):
    for img in image_base_names(folderpath):
        image_set.add(img)


for img in sorted(image_set):
    print(img)

'''
        fparts =  os.path.splitext(img)
        fname_set.add(fparts[0])

'''
    # Make a set of the unique file names - without extensions - for image files in the directory
'''

for f in os.listdir(foldername):
#    if is_valid_image(f.name):
    print(f)
    print(imghdr.what(f))

'''
'''


'''
'''

    '''

'''
    if (imghdr.what(os.path.file=(f)) == 'tiff'):
        fparts =  os.path.splitext(f)
        fname_set.add(fparts[0])

# generate a yaml file for each file name
for fname in sorted(fname_set):
    print(f"ID: {fname}")
    print(f"Scan Date: ")
'''
