import pytest
from utils.api_client import APIClient
import config


# Test GET /posts/1 from JSONPlaceholder

#testcase1
def test_jsonplaceholder_get_post():
    client = APIClient(base_url=config.BASE_URL)
    response = client.request('GET', '/posts/1')
    print("Status:", response.status_code)
    print("Headers:", response.headers)
    print("Text:", response.text)
    assert response.status_code == 200
    data = response.json()
    print("Data:", data)
    assert data['id'] == 1
    assert 'userId' in data

# Test GET /users from JSONPlaceholder

def test_jsonplaceholder_get_users():
    client = APIClient(base_url=config.BASE_URL)
    response = client.request('GET', '/users')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

# Test POST /posts from JSONPlaceholder

def test_jsonplaceholder_create_post():
    client = APIClient(base_url=config.BASE_URL)
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = client.request('POST', '/posts', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == "foo"
    assert data['body'] == "bar"
    assert data['userId'] == 1
    assert 'id' in data

# Test PUT /posts/1 from JSONPlaceholder

def test_jsonplaceholder_update_post():
    client = APIClient(base_url=config.BASE_URL)
    payload = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
    response = client.request('PUT', '/posts/1', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == "updated"
    assert data['body'] == "updated body"
    assert data['id'] == 1

# Test PATCH /posts/1 from JSONPlaceholder

def test_jsonplaceholder_patch_post():
    client = APIClient(base_url=config.BASE_URL)
    payload = {"title": "patched title"}
    response = client.request('PATCH', '/posts/1', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == "patched title"
    assert data['id'] == 1

# Test DELETE /posts/1 from JSONPlaceholder

def test_jsonplaceholder_delete_post():
    client = APIClient(base_url=config.BASE_URL)
    response = client.request('DELETE', '/posts/1')
    # JSONPlaceholder returns 200 for DELETE
    assert response.status_code == 200
    assert response.text == '{}'

# Test GET /get from HTTPBin

def test_httpbin_get():
    client = APIClient(base_url='https://httpbin.org')
    response = client.request('GET', '/get')
    assert response.status_code == 200
    data = response.json()
    assert 'url' in data

# Test POST /post from HTTPBin

def test_httpbin_post():
    client = APIClient(base_url='https://httpbin.org')
    payload = {"test": "data"}
    response = client.request('POST', '/post', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['json'] == payload

# Test PUT /put from HTTPBin

def test_httpbin_put():
    client = APIClient(base_url='https://httpbin.org')
    payload = {"put": "value"}
    response = client.request('PUT', '/put', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['json'] == payload

# Test PATCH /patch from HTTPBin

def test_httpbin_patch():
    client = APIClient(base_url='https://httpbin.org')
    payload = {"patch": "value"}
    response = client.request('PATCH', '/patch', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['json'] == payload

# Test DELETE /delete from HTTPBin

def test_httpbin_delete():
    client = APIClient(base_url='https://httpbin.org')
    response = client.request('DELETE', '/delete')
    assert response.status_code == 200
    data = response.json()
    assert data['url'].endswith('/delete')


# Negative test: GET non-existent resource

def test_jsonplaceholder_get_nonexistent():
    client = APIClient(base_url=config.BASE_URL)
    response = client.request('GET', '/posts/999999')
    # JSONPlaceholder returns empty object for non-existent
    assert response.status_code == 200
    assert response.json() == {} 