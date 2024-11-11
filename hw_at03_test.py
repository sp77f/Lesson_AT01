import pytest
from hw_at03 import get_cat_url

def test_get_catapi_success(mocker):
    mock_get = mocker.patch('hw_at03.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'url': ["https://cdn2.thecatapi.com/images/2oh.gif"]}
    catapi_data = get_cat_url()
    assert catapi_data == {'url': ["https://cdn2.thecatapi.com/images/2oh.gif"]}
def test_get_catapi_error(mocker):
    mock_get = mocker.patch('hw_at03.requests.get')
    mock_get.return_value.status_code = 404
    catapi_data = get_cat_url()
    assert catapi_data is None