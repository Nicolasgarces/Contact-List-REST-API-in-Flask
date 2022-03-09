"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, request
from api.models import db, User, Contact
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/contact/all', methods=['GET'])
def get_contacts():

    data = Contact.query.filter().all()
    all_contacts = list( map(lambda item: item.serialize(), data) )
    print(all_contacts)
    
    return jsonify(all_contacts), 200
#---------------------------------------------------------------------------
# @api.route('/contact', methods=['POST'])
# def create_contact():
#     body = request.get_json()
#     db.session.add(body)
#     db.session.commit()
#     print(body)
#     return jsonify(body), 200
#--------------------------------------------------------------------------------

@api.route('/contact', methods=['POST'])
def create_contact():
    id = request.json.get('id')
    name = request.json.get('full_name')
    email = request.json.get('email')
    address = request.json.get('address')
    phone = request.json.get('phone')
    
    contact = Contact()
    contact.id = id
    contact.full_name = name
    contact.email = email
    contact.address = address
    contact.phone = phone

    db.session.add(contact)
    db.session.commit()
    
    return jsonify(contact.serialize()), 201











#-----------------------------------------------------------------------------------
# @app.route('/members', methods=['POST'])
# def add_new_member():
#     body = request.get_json()
    
#     member = {
#        "id": jackson_family._generateId(),
#         "first_name": body["first_name"],
#         "last_name": jackson_family.last_name,
#         "age": body["age"],
#         "lucky_numbers": body["lucky_numbers"]
#     }
#     result = jackson_family.add_member(member)
#     return jsonify(result), 200

# @app.route('/contacts', methods=['POST'])
# def create_contact():
#     name = request.json.get('name')    
#     email = request.json.get('email')
#     phone = request.json.get('phone')"""
#     data = request.get_json()
#     name = data['name']
#     email = data['email']
#     phone = data['phone']
#      """
#     contact = Contact()
#     contact.name = name
#     contact.email = email
#     contact.phone = phone
#     db.session.add(contact)
#     db.session.commit()
#     return jsonify(contact.serialize()), 201