#!/usr/bin/python
def loaddataintosql():
 f = open("./DBLP_Citation_2014_May/publications.txt")
 lines = f.readlines()	
for line in lines:
    # Split the line on whitespace
    data = line.split()
    number = data[0]
    value = data[1]

    # Put this through to SQL using an INSERT statement...
    cursor.execute("""INSERT INTO tablename (person_id, category, type)
                   VALUES(%s, %s, %s)""", (number, category, value))