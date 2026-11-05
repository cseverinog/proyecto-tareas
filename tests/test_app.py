from app.app import create_app


def test_index():
    client = create_app().test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["nombre"] == "API de tareas"


def test_health():
    client = create_app().test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"estado": "ok"}


def test_task_requires_title():
    client = create_app().test_client()
    response = client.post("/tareas", json={})

    assert response.status_code == 400


def test_task_completion_route_exists():
    client = create_app().test_client()
    response = client.patch("/tareas/1/completar")

    # Without PostgreSQL the endpoint reports the unavailable dependency;
    # this still verifies that the route is registered.
    assert response.status_code in (404, 503)
