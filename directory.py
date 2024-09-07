
class directory:
    def __init__(self, address:str):
        self.address = address
        self.extracted = ''

    def get_all_files(self, containing:str):
        files = {}
        from_dir = self.address
        for filename in glob.iglob(from_dir+'**', recursive=True):
            if os.path.isfile(filename) and containing in filename:
                no_ws = leading_ws_trimmed(filename)
                files[no_ws[3:10]] = filename

        self.extracted = files
        return files
    
    def get_all_subdirs(self):
        subdirs = []
        from_dir = self.address
        for par_subdir in glob.iglob(from_dir+'**\\', recursive=True): #not matched
            if par_subdir.count('\\') == 2: 
                subdirs.append(par_subdir)
        return subdirs
    
    def write_list_to_file(self, file_to_write):
        for file in self.extracted: 
            with open(file_to_write, 'a') as f: 
                f.write(file+'\n')
            count_text = f'FOUND {len(self.extracted)} FILES CONTAINING TARGET PHRASE'
            f.write('#'*len(count_text)+'\n')
            f.write(count_text)
            f.write('#'*len(count_text)+'\n')
                
    def open_folder(self):
        os.system(f"start \"{self.address}\"")
