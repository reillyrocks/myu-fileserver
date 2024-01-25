from fastapi.testclient import TestClient




def test_asdf(client: TestClient) -> None:
    # for route in client.app.routes:
    #     if route.name == "get_train":
    #         path = route.path

    r = client.get("/subway/get_train")
    assert r.json()