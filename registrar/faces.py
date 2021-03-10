import os
import cv2
import numpy as np
from math import sqrt
from registrar import app


def _getLargestFace(faces):
    '''Helper function to select the face with the largest diagonal from a list of faces'''
    if len(faces) == 0: return None

    sizeOf = lambda f: sqrt(f[2]**2 + f[3]**2)
    maxSize = 0
    bigFace = faces[0]
    for face in faces:
        size = sizeOf(face)
        if size > maxSize: maxSize, bigFace = size, face
    return bigFace


def detectFace(photo):
    '''Detects face(s) in a cv2 image'''
    #TODO test using different/multi classifiers
    faceCascade = cv2.CascadeClassifier(os.path.join(app.config['OPENCV'], 'haarcascade_frontalface_default.xml'))
    #TODO optimize parametes
    faces = faceCascade.detectMultiScale(photo, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    return None if len(faces) == 0 else _getLargestFace(faces)


def saveFace(face, image, guid):
    '''Writes the image of a face to a file with a unique ID'''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    success, jpg = cv2.imencode('*.jpg', photo)
    if not success: return False

    path = os.path.join(app.config['DATA'], 'faces', f'{guid}.jpg')
    cv2.imwrite(path, image[face[1]:face[1]+face[3], face[0]:face[0]+face[2]])
    return True
