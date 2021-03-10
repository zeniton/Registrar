from registrar import app, members
import registrar.faces as faces
from uuid import uuid1
from os import path, rename, makedirs
from base64 import b64decode
import numpy as np
import cv2


def test():
    global members
    return members['052450']


def identifyMember(base64photo):
    """Identify the member from a photo
    Returns:
        member object if identified, else None
        GUID of the photo, None if invalid image
    """
    photoGuid, image = _savePhoto(base64photo)
    if photoGuid == None: return None, None

    face = faces.detectFace(image)
    if face == None: return None, None #No face in photo

    if not faces.saveFace(face, image, photoGuid): return None, None #Failed to create jpg
    member = _recogniseMember(image)
    return member, photoGuid


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


def _recogniseMember(npArr):
    #TODO: Implement
    global members
    return members['052450']


def _savePhoto(base64photo):
    """Save the image in the root directory"""
    npArr = np.frombuffer(b64decode(base64photo), dtype=np.uint8)
    img = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    photoGuid = str(uuid1())
    filename = path.join(app.config['DATA'], photoGuid)
    cv2.imwrite(f'{filename}.png', gray)
    return photoGuid, npArr


 