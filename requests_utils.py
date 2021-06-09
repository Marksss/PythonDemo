import requests


def start_request(url, headers=None, params=None, request_type=0):
    if params is None:
        params = {}
    if headers is None:
        headers = {
            # 假装自己是浏览器
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.212 Safari/537.36 '
        }
    try:
        if request_type == 0:
            response = requests.get(url, headers=headers, params=params, timeout=5)
        else:
            response = requests.post(url, headers=headers, params=params, timeout=5)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
    except requests.RequestException:
        return None

