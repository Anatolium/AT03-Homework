import pytest
from main import get_cat_image_url


# Тест, который проверяет успешный запрос и возвращает правильный URL
def test_get_cat_image_url(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id": "ebv",
        "url": "https://cdn2.thecatapi.com/images/ebv.jpg",
        "width": 176, "height": 540,
        "breeds": [],
        "favourite": {}
    }]
    cat_info = get_cat_image_url()

    assert cat_info == [{
        "id": "ebv",
        "url": "https://cdn2.thecatapi.com/images/ebv.jpg",
        "width": 176, "height": 540,
        "breeds": [],
        "favourite": {}
    }]

# Тест, который проверяет неуспешный запрос и возвращает None
def test_get_cat_image_url_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = [{
        "id": "ebv",
        "url": "https://cdn2.thecatapi.com/images/ebv.jpg",
        "width": 176, "height": 540,
        "breeds": [],
        "favourite": {}
    }]
    cat_info = get_cat_image_url()

    assert cat_info == None
