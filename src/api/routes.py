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


@api.route('/contact/all', methods=['GET']) # 1) Obtenga una lista de todos los contactos GET /contact/all
def get_contacts():
    data = Contact.query.filter().all()
    all_contacts = list( map(lambda item: item.serialize(), data) )
    print(all_contacts)
    return jsonify(all_contacts), 200
#-----------------------------------------------------------------------------------------------------------------------------------

@api.route('/contact', methods=['POST']) # 2) Crear un nuevo Contacto POST /contact
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
 #---------------------------------------------------------------------------------------------------------------------------------   

@api.route('/contact/<int:id>', methods=['GET']) # 3) Obtener un Contacto específico (con los objetos del grupo al que pertenece) GET /contact/{contact_id}
def get_contact(id):    
    contact = Contact.query.get(id)  
    print(contact)  
    return jsonify(contact.serialize()), 200
#--------------------------------------------------------------------------------------------------------------------------------

@api.route('/contact/<int:id>', methods=['DELETE']) # 4) Eliminar un Contacto DELETE /contact/{contact_id}
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({}), 200





