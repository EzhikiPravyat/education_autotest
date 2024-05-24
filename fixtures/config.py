import os
from dotenv import load_dotenv
from pytest import fixture
import requests as req
import json

load_dotenv() #вызов функции для подключения env

@fixture()
def env():
    '''
    Получение переменной окружения
    '''
    return os.getenv

@fixture(scope='module')
def session():
    '''
    Подключение и отключение сессии
    '''
    s = req.Session()
    print('\n', "-" * 70, "Session start", "-" * 70)
    yield s
    s.close()
    print('\n', "-" * 70, "Session close", "-" * 70)

@fixture()
def get(headers):
    '''
    GET запрос
    '''
    def req_get(**kwargs):
        kwargs['headers'] = headers
        return req.get(**kwargs)
    return req_get

@fixture()
def post(headers):
    '''
    POST запрос
    '''
    def req_post(**kwargs):
        kwargs['headers'] = headers
        return req.post(**kwargs)
    return req_post

@fixture()
def put(headers):
    '''
    PUT запрос
    '''
    def req_put(**kwargs):
        kwargs['headers'] = headers
        return req.put(**kwargs)
    return req_put

@fixture
def delete(headers):
    '''
    DELETE запрос
    '''
    def req_delete(**kwargs):
        kwargs['headers'] = headers
        return req.delete(**kwargs)
    return req_delete

@fixture()
def headers(env):
    '''
    Передача в headers токена авторизации Authorization
    '''
    return {
        "Authorization": env('token_bearer')
    }


def read_config_json(expected_string):
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    for api_method in config['api_methods']:
        if api_method['endpoint'] == expected_string:
            api_method['url'] = config['URL'] + api_method['endpoint']
            return api_method

    return None