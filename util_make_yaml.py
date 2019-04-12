# Test
import image_metadata_file_maker as file_mkr
params = []
with open('template.txt', 'r') as input:
    params = input.read().splitlines()
fm = file_mkr.ImageMetadataFileMaker('C:/Users/craig/iCloudDrive/Photos/Originals/Scans/_To_Do/test', params)
fm.make_md_file()
