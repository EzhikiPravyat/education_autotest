import os
from dotenv import load_dotenv
from pytest import fixture
import requests as req
import json

load_dotenv() #вызов функции для подключения env

@fixture()
def env():
    return os.getenv

@fixture()
def session():
    s = req.Session()
    yield s
    s.close()

@fixture()
def get(headers):
    def req_get(**kwargs):
        kwargs['headers'] = headers
        return req.get(**kwargs)
    return req_get

@fixture()
def post(headers):
    def req_post(**kwargs):
        kwargs['headers'] = headers
        return req.post(**kwargs)
    return req_post

@fixture()
def put(headers):
    def req_put(**kwargs):
        kwargs['headers'] = headers
        return req.put(**kwargs)
    return req_put

def delete(headers):
    def req_delete(**kwargs):
        kwargs['headers'] = headers
        return req.delete(**kwargs)
    return req_delete

@fixture()
def headers(env):
    return {
        "Authorization": env('token_bearer')
    }

def read_config_json(expected_string):
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    for api_method in config['api_methods']:
        api_method['url'] = config['URL']
        if api_method['endpoint'] == expected_string:
            return api_method

    return None