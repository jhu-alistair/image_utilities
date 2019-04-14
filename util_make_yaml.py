from local_tools import *
from image_metadata_file_maker import ImageMetadataFileMaker
if confirm_config('path'):
    img_path = get_config('path')
    if confirm_template():
        params = get_template()
        fm = ImageMetadataFileMaker(img_path, params)
        fm.make_md_file()
