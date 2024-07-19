import requests

THE_CAT_API_KEY = "live_fTy0RIfPJYRR3CTUfo2MriNMXGckcGyeXFTVGuRXHIUGrCgWpkB3c5EnzdHAViiL"


# Функция, которая делает запрос к TheCatAPI для получения случайного изображения кошки
def get_cat_image_url():
    url = f"https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": THE_CAT_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data[0]["url"]
    else:
        return None
