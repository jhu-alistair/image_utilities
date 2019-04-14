# Image file renamer
from local_tools import *
from image_renamer import ImageRenamer
if confirm_config('path'):
    img_path = get_config('path')
    if confirm_config('image_prefix'):
        prfx = get_config('image_prefix')
        fr = ImageRenamer (img_path, prfx)
        fr.rename_image_files()
