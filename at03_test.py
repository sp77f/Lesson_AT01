import pytest
from at03 import get_weather

def test_get_weather_success(mocker):
    mock_get = mocker.patch('at03.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'weather': [{'description': 'clear sky'}],
                                              'main': {'temp': 280.32}}
    api_key = 'api_key'
    city = 'Moscow'
    weather_data = get_weather(api_key, city)
    assert weather_data == {'weather': [{'description': 'clear sky'}],
                            'main': {'temp': 280.32}}
def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('at03.requests.get')
    mock_get.return_value.status_code = 404
    api_key = 'api_key'
    city = 'Moscow'
    weather_data = get_weather(api_key, city)
    assert weather_data is None