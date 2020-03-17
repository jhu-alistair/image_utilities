'''
ImageMetadataFileEditor

This script walks through the specified directory, identifies yaml files
and attempts to add lines or make changes.

'''

import os
from pathlib import Path
import sys

class ImageMetadataFileMaker:
    def __init__(self, directory_name, source_type):
        self.folder_path = Path.home()  / directory_name
        self.yaml_files = ()

        try:
            # only proceed if path is valid
            assert Path.exists(self.folder_path)
            # create a set of the unique image file base names
            for img in os.listdir(self.folder_path):
                img_path = os.path.join(self.folder_path, img)
                if os.path.isfile(img_path):
                    if (imghdr.what(img_path) != None): # has a valid image extension
                        # build nested dictorary of image file names and attributes
                        img_name = os.path.splitext(img)[0]
                        # build a set of unique image names
                        self.image_names.add(img_name)
        except AssertionError:
            print ("Error in class", self.__class__.__name__ , " -- Calling function provided an invalid path:", self.folder_path)
            raise


    # iterator for list of image file names with extensions
    def image_file_names(self):
        for img in sorted(self.image_names):
            yield img

    def make_md_file(self):
        for fname in self.image_file_names():
            full_name = fname + ".yaml"
            new_file_path = os.path.join(self.folder_path, full_name)
            try:
                with open(new_file_path,'x') as new_file:
                    new_file.write("ID: {0}\n".format(fname))
                    new_file.write("Source Type: {0}\n".format(self.source_type))
                    for fld in self.yaml_fields:
                        new_file.write("{0}: \n".format(fld))
            except FileExistsError:
                print ("Class", self.__class__.__name__ ,  "Error message: file named", fname, "already exists. Skipping file creation.")
            except:
                print ("Error in class", self.__class__.__name__ ,  sys.exc_info()[0])
