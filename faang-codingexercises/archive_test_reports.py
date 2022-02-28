'''
This file is part of the management utility for this coding challenge project.

We zip the test_reports folder each time .
'''

# importing required modules
from zipfile import ZipFile
import os
import datetime
def get_all_file_paths(directory):

	# initializing empty file paths list
	file_paths = []

	# crawling through directory and subdirectories
	for root, directories, files in os.walk(directory):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)

	# returning all file paths
	return file_paths		

def un_zipFiles(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = ZipFile(filePath)
            for names in zip_file.namelist():
                zip_file.extract(names,path)
            zip_file.close() 

def remove_files(path):
    # remove directory contents
    dir = "./test_reports"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
def main():
    # path to folder which needs to be zipped
    directory = './test_reports'

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # specifying the zip file name
    output_file_name = "test_report_files.zip"
    
	# printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile, override file if exists
    with ZipFile(output_file_name,'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')		

    # opening the zip file in READ mode
    with ZipFile(output_file_name, 'r') as zip:
        for info in zip.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')


if __name__ == "__main__":
	main()
