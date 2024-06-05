from flask import Blueprint, request, jsonify
from management_pembimbing.controller.managementcontroller import managementcontroller

management_routes = Blueprint('management_routes', __name__)
management_controller = managementcontroller()

@management_routes.route('/management',methods=['GET'])
def lihat_management():
    if request.method == 'GET':
        return jsonify(management_controller.lihat_management())
    
@management_routes.route('/management/<int:id>',methods=['GET'])
def cari_management(id):
    return management_controller.cari_management(id)

@management_routes.route('/management',methods=['POST'])
def tambah_management():
    data = request.json
    return management_controller.tambah_management(data)

@management_routes.route('/management/<int:id>',methods=['PUT'])
def update_management(id):
    data = request.json
    return management_controller.update_management(id,data)
    