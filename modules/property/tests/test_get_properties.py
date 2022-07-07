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
        assert len(response_json) == 5

    @staticmethod
    def test_get_properties_by_city():
        filter_city = "?city=bogota"
        response = requests.get(url=url + filter_city)
        response_json = json.loads(response.text)
        response_json = response_json[0]
        assert "bogota" in response_json["city"]

    @staticmethod
    def test_get_properties_by_actual_state():
        filter_state = "?actual_state=vendido"
        response = requests.get(url=url + filter_state)
        response_json = json.loads(response.text)
        response_json = response_json[0]
        assert "vendido" in response_json["actual_state"]

