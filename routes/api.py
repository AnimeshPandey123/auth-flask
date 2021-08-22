from flask import Blueprint
from controllers.LoginController import login


api = Blueprint('api', __name__)
api.route('/login', methods=['POST'])(login)