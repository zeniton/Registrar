from registrar import app
from uuid import uuid1
from os import path
from base64 import b64decode
import numpy as np
import cv2

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
    return { 'id': '052450', 'name': 'Stoffel', 'surname': 'van Aswegen' }


def registerMember(member, photoGuid):
    """Record the member's presence at the meeting
    Returns:
        member object if identified, else None
    """
    return None


def _savePhoto(base64photo):
    """Save the image in the root directory"""
    # try:
    npArr = np.frombuffer(b64decode(base64photo), dtype=np.uint8)
    img = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # except:
    #     return None, None

    photoGuid = str(uuid1())
    filename = path.join(app.config['DATA'], photoGuid)
    cv2.imwrite(f'{filename}.png', gray)
    return photoGuid, npArr
