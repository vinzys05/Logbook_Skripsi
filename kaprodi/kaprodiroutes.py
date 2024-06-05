from flask import Blueprint, request, jsonify
from kaprodi.controller.kaprodicontroller import kaprodicontroller

kaprodi_routes = Blueprint('kaprodi_routes', __name__)
kaprodi_controller = kaprodicontroller()

@kaprodi_routes.route('/kaprodi',methods=['GET'])
def lihat_kaprodi():
    if request.method == 'GET':
        return jsonify(kaprodi_controller.lihat_kaprodi())
    
@kaprodi_routes.route('/kaprodi/<int:id>',methods=['GET'])
def cari_kaprodi(id):
    return kaprodi_controller.cari_kaprodi(id)

@kaprodi_routes.route('/kaprodi',methods=['POST'])
def tambah_kaprodi():
    data = request.json
    return kaprodi_controller.tambah_kaprodi(data)

@kaprodi_routes.route('/kaprodi/<int:id>',methods=['PUT'])
def update_kaprodi(id):
    data = request.json
    return kaprodi_controller.update_kaprodi(id,data)