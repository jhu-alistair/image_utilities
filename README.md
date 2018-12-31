# image_utilities

Image Renamer
This class reads the specified directory, identifies all image files using imghdr,
and renames them using the specified prefix string plus a date stamp plus a 4-digit
counter to file names like KFM_2018-12-30_0001. The file extension is not changed.
The process is designed to be idempotent: it will not rename files that already have
names in this format, and it checks for existing files with the specified prefix and
today's date stamp when setting the starting value for the counter.
