# Test
import image_directory as img_mod
img = img_mod.ImageDirectory('Desktop/_Alistair/photos/scans')


img.rename_image_files("DRM04")

'''
for nm in img.unique_image_names():
    print(nm)


for f in img.image_files():
    print(f)

    '''
