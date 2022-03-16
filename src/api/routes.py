"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, jsonify, url_for, Blueprint, request
from api.models import db, User, Contact, Group
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# 1) Obtenga una lista de todos los contactos GET /contact/all
@api.route('/contact/all', methods=['GET']) 
def get_contacts():
    data = Contact.query.filter().all()
    all_contacts = list( map(lambda item: item.serialize(), data) )
    print(all_contacts)
    return jsonify(all_contacts), 200
#-----------------------------------------------------------------------------------------------------------------------------------
# 2) Crear un nuevo Contacto POST /contact
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
 #---------------------------------------------------------------------------------------------------------------------------------   
# 3) Obtener un Contacto específico (con los objetos del grupo al que pertenece) GET /contact/{contact_id}
@api.route('/contact/<int:id>', methods=['GET']) 
def get_contact(id):    
    contact = Contact.query.get(id)  
    print(contact)  
    return jsonify(contact.serialize()), 200
#--------------------------------------------------------------------------------------------------------------------------------
 # 4) Eliminar un Contacto DELETE /contact/{contact_id}
@api.route('/contact/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({}), 200
#-----------------------------------------------------------------------------------------------------------------------------------
# 5) Update a Contact UPDATE /contact/{contact_id} FALTA!!!!!!
@api.route('/contact/<int:id>', methods=['PUT']) 
def update_contact(id):    
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
    # return jsonify(contact.serialize()), 200

#-------------------------------------------------------------------------------------------------------------------------------------
# 6) Get a list of all the Group names and ids GET /group/all
@api.route('/group/all', methods=['GET']) 
def get_groups():
    data = Group.query.filter().all()
    all_groups = list( map(lambda item: item.serialize(), data) )
    print(all_groups)
    return jsonify(all_groups), 200

#-----------------------------------------------------------------------------------------------------------------------------------
# 7) Create a new Group POST /group
@api.route('/group', methods=['POST']) 
def create_group():
    id = request.json.get('id')
    name = request.json.get('name')
    
    group = Group()
    group.id = id
    group.name = name
  
    db.session.add(group)
    db.session.commit()
    
    return jsonify(group.serialize()), 201

#------------------------------------------------------------------------------------------
# 8) Get a specific Group (with all Contact objects related to it) GET /group/{group_id}
@api.route('/group/<int:id>', methods=['GET']) 
def get_group(id):    
    group = Group.query.get(id)  
    print(group)  
    return jsonify(group.serialize()), 200
#--------------------------------------------------------------------------------------------------
# 9) Update a Group name UPDATE /group/{group_id} FALTA!!!
@api.route('/group/<int:id>', methods=['PUT']) 
def update_group(id):    
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
    # return jsonify(contact.serialize()), 200
#--------------------------------------------------------------------------------------------------
#10) Delete a Group DELETE /group/{group_id}
@api.route('/group/<int:id>', methods=['DELETE'])
def delete_group(id):
    group = Group.query.get(id)
    db.session.delete(group)
    db.session.commit()
    return jsonify({}), 200
  



