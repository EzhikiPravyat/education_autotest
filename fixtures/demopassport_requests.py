from pytest import fixture
import requests as req


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