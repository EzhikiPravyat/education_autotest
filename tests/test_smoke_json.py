from jsonschema import validate
from pytest import mark
from fixtures.read_json import read_config_json

@mark.usefixtures('session')
def test_put_user_profile(put, valid_scheme_put_user_profile):
    config_data = read_config_json("/api/v2/user/profile")
    response = put(url=config_data['url'], json=config_data['body'])
    print(response.content)

    assert response.status_code in (200, 401)
    if response.status_code == 200:
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[0])
    else:
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[1])