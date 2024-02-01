from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == "opening hours of a restaurant"


params = {
    "params": {
        "monday": [],
        "tuesday": [{"type": "open", "value": 3600}, {"type": "close", "value": 32400}],
        "wednesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 32400},
        ],
        "thursday": [],
        "friday": [{"type": "open", "value": 64800}],
        "saturday": [
            {"type": "close", "value": 82800},
            {"type": "close", "value": 3600},
            {"type": "open", "value": 32400},
            {"type": "close", "value": 39600},
            {"type": "open", "value": 57600},
        ],
        "sunday": [],
    }
}


def test_post_opening_hour():
    response = client.post(url="/items", json=params)

    assert response.status_code == 200
    assert (
        response.json()
        == "monday: close\ntuesday: 01:00 AM - 09:00 AM\nwednesday: 01:00 AM - 09:00 AM\nthursday: close\nfriday: 18:00 PM - 01:00 AM\nsaturday: 09:00 AM - 11:00 AM, 16:00 PM - 23:00 PM\nsunday: close\n"
    )
