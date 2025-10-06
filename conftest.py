import os
import sys
import pytest

# Add project root to sys.path to import from utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.api_client import APIClient

@pytest.fixture(scope="session")
def client():
    base_url = "https://reqres.in/api"
    return APIClient(base_url)
