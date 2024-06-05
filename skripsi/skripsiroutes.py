from flask import Blueprint, request, jsonify
from skripsi.controller.skripsicontroller import skripsicontroller

skripsi_routes = Blueprint('skripsi_routes', __name__)
skripsi_controller = skripsicontroller()

@skripsi_routes.route('/skripsi',methods=['GET'])
def lihat_skripsi():
    if request.method == 'GET':
        return jsonify(skripsi_controller.lihat_skripsi())
    
@skripsi_routes.route('/skripsi/<int:id>',methods=['GET'])
def cari_skripsi(id):
    return skripsi_controller.cari_skripsi(id)

@skripsi_routes.route('/skripsi',methods=['POST'])
def tambah_skripsi():
    data = request.json
    return skripsi_controller.tambah_skripsi(data)

@skripsi_routes.route('/skripsi/<int:id>',methods=['PUT'])
def update_skripsi(id):
    data = request.json
    return skripsi_controller.update_skripsi(id,data)
    
    