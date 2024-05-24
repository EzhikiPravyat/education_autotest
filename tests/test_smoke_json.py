from jsonschema import validate
from pytest import mark
from fixtures.etp_requests import read_config_json

@mark.usefixtures('session')
def test_put_user_profile(put):
    config_data = read_config_json("/api/v2/user/profile")
    response = put(url=config_data['url'], json=config_data['body'])

    assert response.status_code in (200, 401)
    validate(instance=response.json(), schema=config_data['valid_scheme'])
    
@mark.usefixtures('session')
def test_get_dictionaries_oksm(get):
    config_data = read_config_json("/api/v2/dictionaries/oksm")
    response = get(url=config_data['url'])
    assert response.status_code in (200, 401)
