from fastapi.testclient import TestClient
from fastapp.main import app



client = TestClient(app)





# def test_asdf(client: TestClient) -> None:
def test_asdf() -> None:
    # for route in client.app.routes:
    #     if route.name == "get_train":
    #         path = route.path

    r = client.get("/subway/get_train")
    assert r.json()