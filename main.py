import os
import pathlib, glob, shutil, csv
from pathlib import Path 
import datetime

import argparse
from argparse import ArgumentParser

import employee
import active
import inactive 
import in_progress 
import directory 

#assumes that to_dir contains only folders named in the following format: '7-digit ID LastName, FirstName'

success_log = 'success_log.txt'
failure_log = 'failure_log.txt'

current_year = datetime.date.today().year

def leading_ws_trimmed(string): 
    if string[3] == ' ': 
        new_string = ''.join([string[i] for i in range(len(string)) if i != 3])
        return new_string
    return string

def main():
    ArgumentParser.add_arguments('from_dir')
    ArgumentParser.add_arguments('to_dir')
    
    Downloaded = directory(from_dir)

    #searching for signed letters
    all_files = Downloaded.get_all_files(f'SIGNED {current_year}')

    Active = directory(to_dir)

    #get all dest folders
    all_active = Active.get_all_subdirs()

    #build
    all_employees = {}
    for employee_subdir in all_employees:  
        new_emp = employee_file(employee_subdir)
        all_employees[new_emp.ID] = new_emp

if __name__=="__main__":
    main()
