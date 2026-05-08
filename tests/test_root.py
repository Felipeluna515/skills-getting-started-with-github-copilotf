"""Tests for root endpoint"""

def test_root_serves_index(client):
    """Test that GET / serves the index.html page"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Mergington High School" in response.text