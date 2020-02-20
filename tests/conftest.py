import pytest
import sys

sys.path.append('.')
from hello_world import api as hw_api

@pytest.fixture
def api():
    """
    """
    api = hw_api
    return api

@pytest.fixture
def client():
    """
    """
    api = hw_api
    client = api.test_client()
    yield client
