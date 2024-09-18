import pickle 
import os 
import pathlib
from pathlib import path 

class DB:
    def __init__(self):
        store = {}

    def build_db(self, src_folders):
        for subdir in src_folders:
            new_file = clin_fac_file(clin_fac_subdir)
            self.store[new_fac.ID] = new_fac
   
    def get_store(self):
        return self.store
   
    def dump(self):
        with open('db.txt', 'wb') as h:
            pickle.dump(self.store, h)
    
    def load(self): 
        with open('db.txt', 'rb') as h: 
            pickle.load(self.store, h)