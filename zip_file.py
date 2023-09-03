import os
import sys
import pathlib
import zipfile

dirname = input("Enter directory name that you want to backup :")
if not os.path.isdir(dirname):
    print('Directory',dirname,'does not found')
    sys.exit(0)

curDir = pathlib.Path(dirname)
with zipfile.ZipFile('myzip.zip',mode='w') as archive:
    for file_path in curDir.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDir))

if os.path.isfile("myzip.zip"):
    print("Archive myzip.zip created sucessfully")
else:
    print("Error in creating zip archive")