'''
This script walks through the specified directory, identifies tiff image files and
creates a yaml side-car medatada file for each file base. The script populates the image file
name and the image file creation date. The rest of the yaml file is a standard
template.
'''
import os
from pathlib import Path
import imghdr

md_elements = []

def isImageExtension( ext ):
    # Is the string ext a member of our set of image file extenstions?
    ext_set = {'.tif', '.tiff', '.jpg', '.jpeg', '.png'}
    return (ext.lower() in ext_set);

# Set the folder path
foldername = Path.home()  / 'Desktop/_Alistair/photos/scans'

(Path.exists(foldername))
print(foldername)

'''
foldername = Path(os.path.expanduser('~') + '\Desktop\_Alistair\photos\scans')
print("Directory name is : " + PosixPath(foldername))

'''
'''
# Make a set of the unique file names - without extensions - for image files in the directory
fname_set = set()
for f in os.listdir(foldername):
    print(f)
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
