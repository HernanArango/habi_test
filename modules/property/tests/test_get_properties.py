from http import HTTPStatus
import requests
import json
import config

url = f"http://{config.BASE_URL}:{config.PORT}"


class TestProperties:

    @staticmethod
    def test_get_properties_ok():
        response = requests.get(url=url)
        assert response.status_code == HTTPStatus.OK

    @staticmethod
    def test_get_properties_visible_fields():
        response = requests.get(url=url)
        response_json = json.loads(response.text)
        response_json = response_json[0]
        assert "address" in response_json
        assert "city" in response_json
        assert "price" in response_json
        assert "description" in response_json
        assert "actual_state" in response_json
