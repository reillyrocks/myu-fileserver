import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from fastapp.main import app


os.environ["TESTING"] = "false"


@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        yield c
