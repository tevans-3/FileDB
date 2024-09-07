
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
