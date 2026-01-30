import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)  # ejaze request az domain haye mokhtalef

# ijad object az FamilyStructure
jackson_family = FamilyStructure("Jackson")

# error handler ke error ha ro JSON mikone
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# sitemap baraye didan hame route ha
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET /members
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()  # gereftan tamame member ha
    return jsonify(members), 200

# POST /members
@app.route('/members', methods=['POST'])
def create_member():
    body = request.get_json()  # gereftan JSON az body request
    new_member = jackson_family.add_member(body)  # ezafe kardan be family
    return jsonify(new_member), 200

# GET /members/<id>
@app.route('/members/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"msg": "Miembro no encontrado"}), 404
    return jsonify(member), 200

# DELETE /members/<id>
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if not deleted:
        return jsonify({"msg": "Miembro no encontrado"}), 404
    return jsonify({"done": True}), 200

# run server
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)