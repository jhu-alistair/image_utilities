# List files in a directory. Useful for testing the path
import image_renamer as file_lstr
fl = file_lstr.ImageRenamer ('C:/Users/craig/iCloudDrive/Photos/Originals/Scans/_To_Do/2019_03_11')
for ff in fl.image_files():
    print(ff)
