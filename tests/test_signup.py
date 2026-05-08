"""Tests for signup and unregister endpoints"""

def test_signup_success(client):
    """Test successful signup"""
    response = client.post("/activities/Chess Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]
    assert "newstudent@mergington.edu" in data["message"]


def test_signup_duplicate(client):
    """Test signing up for same activity twice"""
    # First signup
    client.post("/activities/Chess Club/signup?email=dup@mergington.edu")
    
    # Second signup should fail
    response = client.post("/activities/Chess Club/signup?email=dup@mergington.edu")
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]


def test_signup_invalid_activity(client):
    """Test signup for non-existent activity"""
    response = client.post("/activities/NonExistent/signup?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]


def test_unregister_success(client):
    """Test successful unregister"""
    # First signup
    client.post("/activities/Programming Class/signup?email=removeme@mergington.edu")
    
    # Then unregister
    response = client.delete("/activities/Programming Class/signup?email=removeme@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "Unregistered" in data["message"]


def test_unregister_not_signed_up(client):
    """Test unregistering someone not signed up"""
    response = client.delete("/activities/Chess Club/signup?email=notsigned@mergington.edu")
    assert response.status_code == 400
    data = response.json()
    assert "not signed up" in data["detail"]


def test_unregister_invalid_activity(client):
    """Test unregister from non-existent activity"""
    response = client.delete("/activities/NonExistent/signup?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]