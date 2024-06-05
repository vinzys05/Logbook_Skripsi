from flask import Blueprint, request, jsonify
from user.controller.admincontroller import admincontroller

admin_routes = Blueprint('admin_routes', __name__)
admin_controller = admincontroller()

@admin_routes.route('/admin',methods=['GET'])
def lihat_admin():
    if request.method == 'GET':
        return jsonify(admin_controller.lihat_admin())
    
@admin_routes.route('/admin',methods=['POST'])
def tambah_admin():
    data = request.json
    return admin_controller.tambah_admin(data)