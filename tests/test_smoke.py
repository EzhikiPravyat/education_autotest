import requests as req
import pytest

def test_get_oksm(get):
    url = 'https://demo-passport.etpgpb.ru/api/v2/dictionaries/oksm'

    response = get(url=url)
    response_json = response.json()
    print(response.status_code)
    print(response.content)

    try:
        assert response.status_code == 200, 'Status code is 200'
        assert response.headers['content-type'] == 'application/json', f'content-type is application/json'
        assert response_json['errors'] == None, f'Errors in None'
        assert type(response_json['requestId']) == str, f'requestId is string'
    except:
        pytest.fail