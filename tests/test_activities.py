"""Tests for GET /activities endpoint"""

def test_get_activities_returns_success(client):
    """Test that /activities returns 200 and data"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) >= 3  # At least the original activities


def test_get_activities_structure(client):
    """Test that each activity has required fields"""
    response = client.get("/activities")
    data = response.json()
    
    # Check first activity
    activity_name = next(iter(data.keys()))
    activity = data[activity_name]
    
    required_fields = ["description", "schedule", "max_participants", "participants"]
    for field in required_fields:
        assert field in activity
    
    assert isinstance(activity["participants"], list)
    assert isinstance(activity["max_participants"], int)