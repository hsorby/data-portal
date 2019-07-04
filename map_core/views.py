# map_core/views.py
 
#################
#### imports ####
#################
 
from app import app
from flask import render_template, Blueprint, request,make_response, url_for, jsonify, send_from_directory, redirect
from logger import logger
import requests
import json

################
#### config ####
################
 
map_core_blueprint = Blueprint('map_core', __name__, template_folder='templates', url_prefix='/map', static_folder='static')

################
#### routes ####
################


@map_core_blueprint.route('/')
def index():
    return render_template('map_core.html')


@map_core_blueprint.route('models/<path:p>')
def getModels(p):
    url = 'map/static/models/{0}'.format(p)
    return redirect(url)


def post_response_from_remote(url, data=None):
    try:
        session = requests.Session()
        r = session.post(url, data=data)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    resp = make_response(r.content)
    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))
    return resp


def getResponseFromRemote(url, headers=None):
    try:
        session = requests.Session()
        if headers:
            session.headers.update(headers)
        r = session.get(url, cookies=request.cookies)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    resp = make_response(r.content)
    if r.cookies.get('sessionid'):
        resp.set_cookie('sessionid', r.cookies.get('sessionid'))
    return resp


def ensure_string(data):
    if type(data) == bytes:
        string = data.decode()
    else:
        string = data

    return string


@map_core_blueprint.route('staging_model/<path:p>')
def getStagingModel(p):
    url = 'https://staging.physiomeproject.org/workspace/{0}'.format(p)
    return getResponseFromRemote(url)


@map_core_blueprint.route('scaffoldmaker/<path:p>')
def scaffoldmakerproxy(p=''):
    url = 'http://localhost:6565/{0}?{1}'.format(p, str(request.query_string, 'utf-8'))
    return getResponseFromRemote(url)


@map_core_blueprint.route('knowledgebase/<path:data_set>')
def knowledge_base_proxy(data_set=''):
    query_string = ensure_string(request.query_string)
    url = 'https://scicrunch.org/api/1/dataservices/federation/data/{0}?{1}'.format(data_set, query_string, 'utf-8')
    return getResponseFromRemote(url)


@map_core_blueprint.route('biolucida/<path:api_method>', methods=['GET', 'POST'])
def biolucida_client_proxy(api_method=''):
    url = 'https://sparc.biolucida.net/api/v1/{0}'.format(api_method, 'utf-8')
    if request.method == 'POST':
        return post_response_from_remote(url, data=json.loads(request.data))
    else:
        return getResponseFromRemote(url, headers={'token': request.headers['token']})
