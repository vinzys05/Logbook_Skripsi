from flask import Blueprint, request, jsonify
from Logbook.controller.logbookcontroller import logbookController

logbook_routes = Blueprint('logbook_routes', __name__)
logbook_controller = logbookController()

@logbook_routes.route('/logbook', methods=['GET'])
def lihat_logbook():
    if request.method == 'GET':
        return jsonify(logbook_controller.lihat_logbook())
    
@logbook_routes.route('/logbook/<int:id>', methods=['GET'])
def cari_logbook(id):
    return logbook_controller.cari_logbook(id)

@logbook_routes.route('/logbook',methods=['POST'])
def tambah_logbook():
    data = request.json
    return logbook_controller.tambah_logbook(data)

@logbook_routes.route('/logbook/<int:id>',methods= ['PUT'])
def update_logbook(id):
    data = request.json
    return logbook_controller.update_logbook(id,data)

