from jsonschema import validate
from pytest import mark
from fixtures.config import read_config_json


@mark.usefixtures('session') ##Перед запуском теста выполяется предусловие, в данном случае session
def test_put_user_profile(put):
    config_data = read_config_json("/api/v2/user/profile")
    url = config_data['url'] + config_data['endpoint']
    response = put(url=url, json=config_data['body'])

    assert response.status_code == 200 or 401
    validate(instance=response.json(), schema=config_data['valid_scheme'])
    