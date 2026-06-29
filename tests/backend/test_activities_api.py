import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from app import app

client = TestClient(app)


def test_get_activities_returns_all_activities():
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert expected_activity in activities
    assert "participants" in activities[expected_activity]


def test_signup_for_activity_adds_new_participant():
    # Arrange
    activity_name = "Drama Club"
    email = "backend-test-student@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup?email={email}"

    # Act
    response = client.post(signup_url)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    activities = client.get("/activities").json()
    assert email in activities[activity_name]["participants"]
