from flask import Blueprint, request, jsonify
from user.controller.usercontroller import usercontroller

user_routes = Blueprint('user_routes', __name__)
user_controller = usercontroller()

@user_routes.route('/user',methods=['GET'])
def lihat_user():
    if request.method == 'GET':
        return jsonify(user_controller.lihat_user())
    
@user_routes.route('/user',methods=['POST'])
def tambah_user():
    data = request.json
    return user_controller.tambah_user(data)