from requests import get

def test_conn():
    assert get('http://0.0.0.0:5000/').status_code == 200