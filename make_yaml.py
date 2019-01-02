# Test
import image_metadata_file_maker as file_mkr
params = ['Source Type: 35mm slide half frame', 'Creator: Kay Morrison', 'Developer Info: ']
fm = file_mkr.ImageMetadataFileMaker('Desktop/_Alistair/photos/KFM', params)
fm.make_md_file()
