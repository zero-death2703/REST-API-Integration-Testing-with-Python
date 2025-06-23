import requests

class APIClient:
    def __init__(self, base_url, auth=None, headers=None, verify=True):
        self.base_url = base_url.rstrip('/')
        self.auth = auth
        self.headers = headers or {}
        self.verify = verify

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(
            method, url, auth=self.auth, headers=self.headers, verify=self.verify, **kwargs
        )
        print('ok')
        print(f"{method} {url} -> {response.status_code}")
        return response 