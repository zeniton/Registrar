from registrar import app, members
from uuid import uuid1
from os import path, rename, makedirs
from base64 import b64decode
import numpy as np
import cv2
import csv


def test():
    global members
    return members['052450']

def identifyMember(base64photo):
    """Identify the member from a photo
    Returns:
        member object if identified, else None
        GUID of the photo, None if invalid image
    """
    photoGuid, npArr = _savePhoto(base64photo)
    if photoGuid == None:
        return None, None
    else:
        member = _recogniseMember(npArr)
        return member, photoGuid


def _recogniseMember(npArr):
    #TODO: Implement
    global members
    return members['052450']


def registerMember(memberId, photoGuid):
    """Record the member's presence at the meeting
    Returns:
        member object if identified by memberId, else None
    """
    #Move the new face to the member's directory
    memberId = f'{int(memberId):06d}'
    srcDir = path.join(app.config['DATA'], 'faces')
    dstDir = path.join(srcDir, memberId)
    makedirs(dstDir, exist_ok=True)
    rename(path.join(srcDir, photoGuid), path.join(dstDir, photoGuid))

    global members
    return members[memberId] if memberId in members else None 


def _savePhoto(base64photo):
    """Save the image in the root directory"""
    npArr = np.frombuffer(b64decode(base64photo), dtype=np.uint8)
    img = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    photoGuid = str(uuid1())
    filename = path.join(app.config['DATA'], photoGuid)
    cv2.imwrite(f'{filename}.png', gray)
    return photoGuid, npArr


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
 