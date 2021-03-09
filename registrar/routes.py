from flask import request, jsonify
from registrar import app
import registrar.api as api

@app.route('/')
def test():
    return jsonify(message="Welcome to Registrar API"), 200


@app.route('/v1/identify', methods=['POST'])
def identify():
    photo = request.get_json(force=True).get('photo')
    if photo == None: return jsonify(message='No photo provided'), 400

    member, photoGuid = api.identifyMember(photo)
    if photoGuid == None: return jsonify(message='Bad photo'), 400

    payload = { 'photoGuid': photoGuid, 'member': member }
    return jsonify(payload), 404 if member == None else 200

@app.route('/v1/register', methods=['POST'])
def register():
    json = request.get_json(force=True)
    photoGuid = json.get('photoGuid')
    if photoGuid == None: return jsonify(message='Missing photoGuid'), 400
    memberId = json.get('memberId')
    if memberId == None: return jsonify(message='Missing memberId'), 400

    member = api.registerMember(memberId, photoGuid)
    if member == None: return None, 404
    else: return jsonify({ 'member': member }), 200