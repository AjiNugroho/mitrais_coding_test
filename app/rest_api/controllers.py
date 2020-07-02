from flask import Blueprint, request, send_file, render_template
from app.rest_api.models import Database
from helpers.response_builder import resp
from helpers.validator import client_checker
#from flask_cors import CORS, cross_origin
#from app import app
#app.config['CORS_HEADERS'] = 'Content-Type'

#cors = CORS(app)
rest_controller = Blueprint('rest_controller', __name__, url_prefix='/mitrais', template_folder='../../templates')
#---------------------------------------------------------------
@rest_controller.route('/welcome', methods=['GET'])
def welcome(**kwargs):

    return 'welcome'
#---------------------------------------------------------------    

@rest_controller.route('/register',methods=['GET'])
def bukaregister():
    return render_template('mitsignup.html')

@rest_controller.route('/view_login',methods=['GET'])
def bukalogin():
    return render_template('mitlogin.html')

#---------------------------------------------------------------
@rest_controller.route('/save_register',methods=['POST'])
@client_checker(no_auth=True)
def save_to_db(**kwargs):
    request_params = kwargs.get('request_params')
    no_hp = request_params.get('mobile_number')
    email = request_params.get('email')
    first_name = request_params.get('first_name')
    last_name = request_params.get('last_name')
    birth = request_params.get('birth')
    gender = request_params.get('gender')

    #validasi di level api
    if not no_hp or not email or not first_name or not last_name:
        return resp(214)
    #no hp harus 12
    if not len(no_hp) == 12:
        return resp(211)
    #no_hp tidak boleh ada char
    if not no_hp.isdigit():
        return resp(211)

    #no_hp diawali 08
    if not no_hp[:2] == '08':
        return resp(211)
    #email harus ada @ dan titik
    if not '@' in email or not '.' in email:
        return resp(212)

    db = Database(no_hp=no_hp,email=email)
    cek_user = db.get_user_info()
    if cek_user['error_code'] != 0:
        return resp(**cek_user)

    response = db.save_register(first_name,last_name,birth,gender)

    return resp(**response)

@rest_controller.route('/login',methods=['POST'])
@client_checker(no_auth=True)
#@cross_origin()
def login(**kwargs):
    request_params = kwargs.get('request_params')
    no_hp = request_params.get('mobile_number')
    email = request_params.get('email')

    #validasi di level api
    if not no_hp or not email:
        return resp(213)
    #no hp harus 12
    if not len(no_hp) == 12:
        return resp(211)
    #no_hp tidak boleh ada char
    if not no_hp.isdigit():
        return resp(211)

    #no_hp diawali 08
    if not no_hp[:2] == '08':
        return resp(211)
    #email harus ada @ dan titik
    if not '@' in email or not '.' in email:
        return resp(212)

    db = Database(no_hp=no_hp,email=email)
    response = db.login()

    return resp(**response)


