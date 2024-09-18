import os
import pathlib, glob, shutil, csv
from pathlib import Path 
import datetime
import directory
import utilities

class employee: 
    def __init__(self, address:str):
        #address is a string, 'W:\7-DIGIT_ID LASTNAME, FIRSTNAME'
        self.orig_address = address
        address = leading_ws_trimmed(address)
        self.ID = address[3:10]
        self.folder = address[:3]
        self.fullname = address[11:len(address)-1]
        self.tempfilepath = address
        self.all_filepaths = list(filter(lambda y:y.is_file, Path(self.orig_address+'.').iterdir()))
        self.all_filenames = [os.path.basename(fp) for fp in self.all_filepaths]
        self.full_path = os.path.join(self.folder, self.fullname)
        self.file_to_upload = ''
        try: 
            self.firstname = self.fullname.split(',')[1].strip()
        except Exception as IndexError: 
            self.firstname = 'NotFound'
        try: 
            self.lastname = self.fullname.split(',')[0].strip()
        except Exception as IndexError: 
            self.lastname = 'NotFound'
    
    def find_and_process_file_from(self, files, fnm):
        """
        extracts a file from the dictionary of all files,
        renames, and uploads it to that employee's folder in the directory
        """
        
        try:
            file_to_upload = files[self.ID]
            ext = Path(file_to_upload).suffix
            new_fnm = f'{fnm} - {self.lastname.upper()}, {self.firstname.upper()} - {current_year}'+ext
            if new_fnm not in self.all_files: 
                shutil.copy(file_to_upload, self.orig_address+new_fnm)
            result = f'Successfully uploaded document to {self.ID} - {self.firstname} {self.lastname} records.'
            with open(success_log, 'a') as f:
                f.write(result+ ' ' + str(datetime.datetime.now()) + '\n')    
        except Exception as KeyError: 
            result = f'No files found for {self.ID}. Check that the source folder contains a {fnm}.'
            with open(failure_log, 'a') as f:
                f.write(result+' ' + str(datetime.datetime.now()) +'\n') 
            return result