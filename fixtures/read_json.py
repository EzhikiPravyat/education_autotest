from pytest import fixture
import json
import os


def read_config_json(expected_string):
    '''
    Чтение JSOn файла config/config.json
    '''
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    for api_method in config['api_methods']:
        if api_method['endpoint'] == expected_string:
            api_method['url'] = config['URL'] + api_method['endpoint']
            return api_method

    return None