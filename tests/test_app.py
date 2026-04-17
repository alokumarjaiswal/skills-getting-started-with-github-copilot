import pytest


def test_get_activities(test_client):
    # Arrange: (No special setup needed)

    # Act
    response = test_client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities


def test_signup_activity_success(test_client):
    # Arrange
    activity_name = "Art Studio"
    email = "newuser@mergington.edu"

    # Act
    response = test_client.post(
        f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in test_client.get(
        "/activities").json()[activity_name]["participants"]


def test_signup_activity_duplicate(test_client):
    # Arrange
    activity_name = "Art Studio"
    email = "newuser@mergington.edu"

    # Act
    response = test_client.post(
        f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Student already signed up"


def test_signup_activity_not_found(test_client):
    # Arrange
    activity_name = "Nonexistent Club"
    email = "someone@mergington.edu"

    # Act
    response = test_client.post(
        f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Activity not found"
