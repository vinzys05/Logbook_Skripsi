from flask import Blueprint, request, jsonify
from mahasiswa.controller.mahasiswacontroller import mahasiswacontroller

mahasiswa_routes = Blueprint('mahasiswa_routes', __name__)
mahasiswa_controller = mahasiswacontroller()

@mahasiswa_routes.route('/mahasiswa',methods=['GET'])
def lihat_mahasiswa():
    if request.method == 'GET':
        return jsonify(mahasiswa_controller.lihat_mahasiswa())
    
@mahasiswa_routes.route('/mahasiswa/<int:id>',methods=['GET'])
def cari_mahasiswa(id):
    return mahasiswa_controller.cari_mahasiswa(id)

@mahasiswa_routes.route('/mahasiswa',methods=['POST'])
def tambah_mahasiswa():
    data = request.json
    return mahasiswa_controller.tambah_mahasiswa(data)

@mahasiswa_routes.route('/mahasiswa/<int:id>',methods=['PUT'])
def update_mahasiswa(id):
    data = request.json
    return mahasiswa_controller.update_mahasiswa(id,data)
    
    