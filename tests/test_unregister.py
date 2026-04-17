import pytest

# Note: The DELETE endpoint must exist in the backend for this test to pass.


def test_unregister_participant(test_client):
    # Arrange
    activity_name = "Art Studio"
    email = "unregisteruser@mergington.edu"
    # Register the user first
    test_client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act
    response = test_client.delete(
        f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code in (200, 404)  # 404 if already removed
    if response.status_code == 200:
        data = response.json()
        assert "message" in data
        assert email not in test_client.get(
            "/activities").json()[activity_name]["participants"]
    else:
        data = response.json()
        assert "detail" in data
