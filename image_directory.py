class ImageDirectory:
    def __init__(self, directory_name, image_types):
        import os
        from pathlib import Path
        import imghdr


        self.folder_path = Path.home()  / directory_name
        try:
            assert Path.exists(self.folder_path)
        except AssertionError:
            print ("Error in class", self.__class__.__name__ , " -- Calling function provided an invalid path:", self.folder_path)
#            raise
