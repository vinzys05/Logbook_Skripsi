from flask import Blueprint, request, jsonify
from dosendanprodi.controller.dosencontroller import dosencontroller

dosen_routes = Blueprint('dosen_routes', __name__)
dosen_controller = dosencontroller()

@dosen_routes.route('/dosen',methods=['GET'])
def lihat_dosen():
    if request.method == 'GET':
        return jsonify(dosen_controller.lihat_dosen())
    
@dosen_routes.route('/dosen/<int:id>',methods=['GET'])
def cari_dosen(id):
    return dosen_controller.cari_dosen(id)

@dosen_routes.route('/dosen',methods=['POST'])
def tambah_dosen():
    data = request.json
    return dosen_controller.tambah_dosen(data)

@dosen_routes.route('/dosen/<int:id>',methods=['PUT'])
def update_dosen(id):
    data = request.json
    return dosen_controller.update_dosen(id,data)

@dosen_routes.route('/dosen/<int:id>',methods=['DELETE'])
def hapus_dosen(id):
    return dosen_controller.hapus_dosen(id)