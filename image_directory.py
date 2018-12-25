# trying as a module
import os
from pathlib import Path
import imghdr
import datetime
import re

class ImageDirectory:

    def __init__(self, directory_name):
        self.image_files_attrs = {} # nested dictionary of image file names and their attributes
        self.image_names = set()    # image file names without extensions
        self.folder_path = Path.home()  / directory_name
        self.dt_stamp = datetime.datetime.now().strftime("%Y-%m-%d") # date stamp for file renaming
        self.name_map = {} # maps current image file names (without extension) to new names

        try:
            # only proceed if path is valid
            assert Path.exists(self.folder_path)

            # create a set of the unique image file base names
            # and a set of the full image file names
            for img in os.listdir(self.folder_path):
                img_path = os.path.join(self.folder_path, img)
                if os.path.isfile(img_path):
                    if (imghdr.what(img_path) != None): # has a valid image extension
                        # build nested dictorary of image file names and attributes
                        pref, suf = os.path.splitext(img)
                        typ = imghdr.what(img_path)
                        self.image_files_attrs[img] = {'prefix': pref, 'suffix': suf, 'img_type': typ}
                        # build a set of unique image names
                        self.image_names.add(pref)
        except AssertionError:
            print ("Error in class", self.__class__.__name__ , " -- Calling function provided an invalid path:", self.folder_path)

    # iterator for list of image file names with extensions
    def image_files(self):
        for f in self.image_files_attrs.keys():
            yield f


    # replace image file names with date stamp plus counter
    def rename_image_files(self, prefix):
        ctr = 0
        for img in self.image_names:
            if not self.is_a_datestamp(img):
                ctr += 1
                self.name_map[img] = prefix + "_" + self.dt_stamp + "_" + f"{ctr:04}"
        if self.name_map:
            for old_file_name in self.image_files():
                old_prefix = self.image_files_attrs[old_file_name]['prefix']
                # since we skipped over files names that are already dates stamps do a check
                if self.name_map.get(old_prefix, False):
                    new_file_name = self.name_map[old_prefix] + self.image_files_attrs[old_file_name]['suffix']
                    print(old_file_name + " => " + new_file_name)

        else: print("There are no image files that do no already have names based on date stamp in", self.folder_path)

    # check that string contains a valid date in iso format
    def is_a_datestamp(self, val):
        match_obj = re.search( r'\d{4}-\d{2}-\d{2}', val)
        if match_obj != None:
            try:
                match_string = match_obj.group()
                test_date = datetime.datetime.strptime(match_string, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        else: return False
