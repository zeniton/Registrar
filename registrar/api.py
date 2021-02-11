from registrar import app
from uuid import uuid1
from os import path
from base64 import b64decode
import numpy as np
import cv2


def identifyMember(photo):
    photoId, npArr = _saveNewPhoto(photo)
    member = recogniseMember(npArr)
    return member, photoId


def recogniseMember(npArr):
    return None


def registerMember(member, photoId):
    pass


def _saveNewPhoto(photo):
    photoId = str(uuid1())
    filename = path.join(app.config["DATA"], photoId)
    npArr = np.frombuffer(b64decode(photo), dtype=np.uint8)
    img = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{filename}.png', gray)
    return photoId, npArr
