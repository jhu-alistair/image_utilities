# List files in a directory. Useful for testing the path
from local_tools import *
from image_renamer import ImageRenamer
if confirm_config('path'):
    img_path = get_config('path')
    fl = ImageRenamer(img_path)
    for ff in fl.image_files():
        print(ff)
