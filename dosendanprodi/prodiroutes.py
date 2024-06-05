from flask import Blueprint, request, jsonify
from dosendanprodi.controller.prodicontroller import prodicontroller

prodi_routes = Blueprint('prodi_routes', __name__)
prodi_controller = prodicontroller()

@prodi_routes.route('/prodi',methods=['GET'])
def lihat_prodi():
    if request.method == 'GET':
        return jsonify(prodi_controller.lihat_prodi())
    
@prodi_routes.route('/prodi',methods=['POST'])
def tambah_prodi():
    data = request.json
    return prodi_controller.tambah_prodi(data)

@prodi_routes.route('/prodi/<int:id>',methods=['PUT'])
def update_prodi(id):
    data = request.json
    return prodi_controller.update_prodi(id,data)

@prodi_routes.route('/prodi/<int:id>',methods=['DELETE'])
def hapus_prodi(id):
    return prodi_controller.hapus_prodi(id)
