# Test
import image_metadata_file_maker as file_mkr
params = ['Source Type: 35mm slide', 'Creator: Kay Morrison', 'Developer Info: Kodachrome TRANSPARENCY', 'Description: ', 'Annotation: ', 'Location: ', 'Date: ', 'Event: ', 'People:']
fm = file_mkr.ImageMetadataFileMaker('C:/Users/craig/iCloudDrive/Photos/Originals/Scans/_To_Do/2019_03_11', params)
fm.make_md_file()
