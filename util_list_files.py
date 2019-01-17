# List files in a directory. Useful for testing the path
import image_renamer as file_lstr
fl = file_lstr.ImageRenamer ('/Users/amorri63/Library/Mobile Documents/com~apple~CloudDocs/Photos/Originals/Photos/_To-Do')
for ff in fl.image_files():
    print(ff)
