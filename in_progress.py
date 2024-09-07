import employee

class in_progress(employee):
    def __init__(self, address:str): 
        clin_fac_file.__init__(self)
        self.active = FALSE 
    
    def __find_and_process_file_from__(self, files, fnm, dir):
        """
        extracts a file from the dictionary of all employee files,
        renames and uploads it to that employee's folder in the directory. 
        """
        try:
            file_to_upload = files[self.ID]
            ext = Path(file_to_upload).suffix
            new_fnm = f'{fnm} - {self.lastname.upper()}, {self.firstname.upper()} - {current_year}'+ext
            shutil.copy(file_to_upload, self.orig_address+new_fnm)
            shutil.move(self.orig_address, dir)
            
            result = f'Successfully uploaded {fnm} to {self.ID} - {self.firstname} {self.lastname} records.\nSuccessfully removed {self.ID}""s record from "In Progress" and uploaded to Active directory."
            with open(success_log, 'a') as f:
                f.write(result+'\n')    
            return result
        except Exception as KeyError: 
            result = f'No files found for {self.ID}. Check that the source folder contains a {fnm}.'
            with open(failure_log, 'a') as f:
                f.write(result+'\n') 
            return result
