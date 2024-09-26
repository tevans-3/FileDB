class DB:
    def __init__(self, src_folders, load_saved=0):
        self.src_folders = src_folders
        if not load_saved: 
            self.store = self.build_db()
        else: 
            self.store = self.load()

    def build_db(self):
        store = {}
        for subdir in self.src_folders:
            new_file = employee(subdir)
            store[new_file.ID] = new_file
        return store
   
    def get_store(self):
        return self.store
   
    def dump(self):
        with open('db.txt', 'wb') as h:
            pickle.dump(self.store, h)
    
    def load(self): 
        with open('db.txt', 'rb') as h: 
            loaded = pickle.load(h)
            return loaded
      
