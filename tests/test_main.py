"""Define Tests."""
from fastapi import status
from fastapi.testclient import TestClient

from api import main


client = TestClient(main.one_repetition_maximum_calc_api)


def test_root():
    """A test case for 'root' endpoint."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World!"}


def test_calc_one_rep_max_valid_values():
    """A test case for 'calc_1rm' endpoint."""
    response = client.post("/api/v1/calc_1rm",
                           json={"weight": 82.5, "reps": 10})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "one_rep_max": 110,
        "weights": [
            {"percentage": 95, "weight": 105},
            {"percentage": 90, "weight": 99},
            {"percentage": 85, "weight": 94},
            {"percentage": 80, "weight": 88},
            {"percentage": 75, "weight": 83},
            {"percentage": 70, "weight": 77},
            {"percentage": 65, "weight": 72},
            {"percentage": 60, "weight": 66},
            {"percentage": 55, "weight": 61},
            {"percentage": 50, "weight": 55},
            {"percentage": 45, "weight": 50},
            {"percentage": 40, "weight": 44},
            {"percentage": 35, "weight": 39},
            {"percentage": 30, "weight": 33},
            {"percentage": 25, "weight": 28},
            {"percentage": 20, "weight": 22},
        ],
    }


def test_calc_one_rep_max_empty_json():
    """A test case that JSON is empty."""
    response = client.post("/api/v1/calc_1rm", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": "Both weight and reps are required."
    }


def test_calc_one_rep_max_not_exist_reps():
    """A test case that reps doesn't exist."""
    response = client.post("/api/v1/calc_1rm", json={"weight": 100})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": "Both weight and reps are required."
    }


def test_calc_one_rep_max_not_exist_weight():
    """A test case that weight doesn't exist."""
    response = client.post("/api/v1/calc_1rm", json={"reps": 5})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": "Both weight and reps are required."
    }


def test_calc_one_rep_max_invalid_type_weight():
    """A test case that weight is an invalid value."""
    response = client.post("/api/v1/calc_1rm",
                           json={"weight": "x", "reps": 3})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "weight"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            }
        ]
    }


def test_calc_one_rep_max_invalid_type_reps():
    """A test case that reps is an invalid value."""
    response = client.post("/api/v1/calc_1rm",
                           json={"weight": 70, "reps": "y"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "reps"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            }
        ]
    }


def test_calc_one_rep_max_both_invalid_type():
    """A test case that weight and reps are both invalid values."""
    response = client.post("/api/v1/calc_1rm",
                           json={"weight": "x", "reps": "y"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "weight"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            },
            {
                "loc": ["body", "reps"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            },
        ]
    }
