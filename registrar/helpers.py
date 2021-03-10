from registrar import app, members
from os import path
import csv


def _readMembers():
    global members
    with open(path.join(app.config['DATA'], 'members', 'members.csv')) as f:
        reader = csv.DictReader(f, quotechar='"')
        for row in reader:
            memberId = row['Mem No'].replace('\t','')
            memberId = f"{int(memberId):06d}"
            member = { 
                'name': row['Preferred Name'],
                'surname': row['Surname'],
                'language': row['Language'][0:1],
                'email': row['E-mail address'],
                'phone': row['Mobile No'].replace('\t','')
                }
            members[memberId] = member
