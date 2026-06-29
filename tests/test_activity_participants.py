import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app


def test_unregister_participant_removes_their_email():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.post(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
