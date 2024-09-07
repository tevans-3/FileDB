
def get_IDs(all_employees):
    for employee in all_employees:
        frst = employee.firstname
        last = employee.lastname
        with open('names_ids.csv') as csvfile: 
            reader = csv.reader(csvfile, dialect='excel')
            for row in reader: 
                if last in row[0].strip() and frst in row[1].strip():
                    employee.ID = row[2]
                    break

def str_isnumeric(string): 
    for char in string: 
        if not char.isnumeric():
            return 0 
    return 1
    
def extract_and_append_IDs(to_dir, from_dir): 
    """
    modify depending on formatting of the searched directory's filenames
    """
    for sub_dir in dir: 
        orig_path = sub_dir 
        sub_dir = sub_dir.split()
    new_path = to_dir 
    new_id = ''
    if len(sub_dir) == 4: 
        Id_str = sub_dir[1]
        if len(Id_str) < 7 and str_isnumeric(Id_str):
            nid += ('0'*(7-len(Id_str)))
            nid += Id_str
            new_path += nid 
            new_path += ' ' +sub_dir[2]
            new_path += ' ' +sub_dir[3]
            os.rename(orig_path, new_path[:-1])
    elif len(sub_dir) == 3: 
        Id_str = sub_dir[0][3:]
        if len(Id_str) < 7 and str_isnumeric(Id_str):
            nid += ('0'*(7-len(Id_str)))
            nid += Id_str
            new_path += nid 
            new_path += ' ' +sub_dir[1]
            new_path += ' ' +sub_dir[2]
            os.rename(orig_path, new_path[:-1])
    try: 
        lname = sub_dir[0][3:].lower().strip()
    except Exception as IndexError: 
        lname = ''
    try: 
        fname = sub_dir[1].lower().strip()[:-1]
    except Exception as IndexError: 
        fname = ''
    
    for active_emp in all_employees:
        new_path = to_dir
        if fname in active_emp.firstname and lname in active_emp.lastname:
            new_path += active_emp.ID + ' ' + active_emp.tempfilepath[3:-1]
            try: 
                os.rename(active_emp.tempfilepath, new_path)
            except Exception as FileNotFoundError: 
                pass
    os.rename()
    for active_emp in all_clin_fac:
        new_path = to_dir
        if fname in active_emp.firstname and lname in active_emp.lastname:
            nid = ''
            if len(str(active_emp.ID)) < 7: 
                nid += ('0'*(7-len(active_emp.ID)))
                nid += active_emp.ID
            else:
                nid = active_emp.ID
            new_path += nid 
