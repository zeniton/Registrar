from http import HTTPStatus
from flask import request, jsonify
from registrar import app
import registrar.api as api

@app.route('/')
def test():
    member = api.test()
    return jsonify(member=member), HTTPStatus.OK
    # return jsonify(message="Welcome to Registrar API"), HTTPStatus.OK


@app.route('/v1/identify', methods=['POST'])
def identify():
    photo = request.get_json(force=True).get('photo')
    if photo == None: return jsonify(message='No photo provided'), HTTPStatus.BAD_REQUEST

    member, photoGuid = api.identifyMember(photo)
    if photoGuid == None: return jsonify(message='Bad photo'), HTTPStatus.BAD_REQUEST

    payload = { 'photoGuid': photoGuid, 'member': member }
    return jsonify(payload), HTTPStatus.NOT_FOUND if member == None else HTTPStatus.OK


@app.route('/v1/register', methods=['POST'])
def register():
    json = request.get_json(force=True)
    photoGuid = json.get('photoGuid')
    if photoGuid == None: return jsonify(message='Missing photoGuid'), HTTPStatus.BAD_REQUEST
    memberId = json.get('memberId')
    if memberId == None: return jsonify(message='Missing memberId'), HTTPStatus.BAD_REQUEST

    member = api.registerMember(memberId, photoGuid)
    return jsonify({ 'member': member }), HTTPStatus.NOT_FOUND if member == None else HTTPStatus.OK