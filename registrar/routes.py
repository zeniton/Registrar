from flask import request, jsonify
from registrar import app
import registrar.api as api

@app.route('/test', methods=['GET'])
def test():
    return jsonify(message="Don't panic"), 200


@app.route('/v1/identify', methods=['POST'])
def identify():
    return jsonify(message="Don't panic"), 200
    photo = request.get_json(force=True).get('photo')
    if photo == None:
        return jsonify(message='No photo provided'), 400

    member, photoGuid = api.identifyMember(photo)
    if photoGuid == None:
        return jsonify(message='Bad photo'), 400

    payload = { 'photoGuid': photoGuid, 'member': member }
    return jsonify(payload), 404 if member == None else 200
