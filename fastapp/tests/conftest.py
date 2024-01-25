from typing import Generator

import pytest
from fastapp.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        yield c
