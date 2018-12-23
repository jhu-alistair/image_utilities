# trying as a module
import os
from pathlib import Path
import imghdr


class ImageDirectory:

    def __init__(self, directory_name):
        self.image_file_names = set()  # image file names with extensions
        self.image_names = set()    # image file names without extensions
        self.folder_path = Path.home()  / directory_name
        try:
            # only proceed if path is valid
            assert Path.exists(self.folder_path)

            # create a set of the unique image file base names
            # and a set of the full image file names
            for img in os.listdir(self.folder_path):
                img_path = os.path.join(self.folder_path, img)
                if os.path.isfile(img_path):
                    if (imghdr.what(img_path) != None): # has a valid image extension
                        self.image_file_names.add(os.path.basename(img_path))
                        self.image_names.add(os.path.splitext(img)[0])

        except AssertionError:
            print ("Error in class", self.__class__.__name__ , " -- Calling function provided an invalid path:", self.folder_path)

    # iterator for list of image file names with extensions
    def image_files(self):
        for fl in self.image_file_names:
            yield fl

    # iterator for list of image unique names without extensions
    def unique_image_names(self):
        for img in self.image_names:
            yield img

    # replace image file names with date stamp plus counter
#    def rename_image_files(self):
