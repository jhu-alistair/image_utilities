'''
Image Renamer
This class reads the specified directory, identifies all image files using imghdr,
and renames them using the specified prefix string plus a date stamp plus a 4-digit
counter to file names like KFM_2018-12-30_0001. The file extension is not changed.
The process is designed to be idempotent: it will not rename files that already have
names in this format, and it checks for existing files with the specified prefix and
today's date stamp when setting the starting value for the counter.

Call it like this, specifying a directory below your user account:
  import image_renamer as img_rename
  img = img_rename.ImageRenamer('Desktop/photos/scans', 'KFM')
  img.rename_image_files()

Created by Alistair Morrison. 2018-12-30.
'''

import os
from pathlib import Path
import imghdr
import datetime
import re

class ImageRenamer:
    def __init__(self, directory_name, new_prefix_code):
        self.image_files_attrs = {} # nested dictionary of image file names and their attributes
        self.image_names = set()    # image file names without extensions
        self.folder_path = Path.home()  / directory_name
        self.new_prefix = new_prefix_code + "_" +  datetime.datetime.now().strftime("%Y-%m-%d")
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
            raise

    # iterator for list of image file names with extensions
    def image_files(self):
        for f in self.image_files_attrs.keys():
            yield f

    # replace image file names with date stamp plus counter
    def rename_image_files(self):
        ctr = self.set_ctr()
        for img in self.image_names:
            if not self.is_a_datestamp(img):
                print(img)
                ctr += 1
                self.name_map[img] = self.new_prefix + "_" + f"{ctr:04}"
        if self.name_map:
            for old_file_name in self.image_files():
                old_prefix = self.image_files_attrs[old_file_name]['prefix']
                # since we skipped over files names that are already dates stamps do a check
                if self.name_map.get(old_prefix, False):
                    new_file_name = self.name_map[old_prefix] + self.image_files_attrs[old_file_name]['suffix']
                    print(old_file_name + " => " + new_file_name)
                    old_file_path = os.path.join(self.folder_path, old_file_name)
                    new_file_path = os.path.join(self.folder_path, new_file_name)
                    os.rename(old_file_path, new_file_path)

        else: print("There are no image files that do no already have names based on date stamp in", self.folder_path)

    # check that string contains a valid date in iso format
    def is_a_datestamp(self, val):
        match_obj = re.search(r"(\d{4}-\d{2}-\d{2})(_\d{4})", val)
        if match_obj != None:
            try:
                match_string = match_obj.group(1)
                test_date = datetime.datetime.strptime(match_string, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        else: return False

    # set the counter to the highest number that has already been used with the new file name pattern and today's date
    def set_ctr(self):
        ctr_list = []
        for f in self.image_files():
            match_obj = re.search(re.escape(self.new_prefix) + r"(_)(\d{4})", f)
            if match_obj != None:
                ctr_list.append(match_obj.group(2))
        if ctr_list:
            return int(max(ctr_list))
        else: return 1
