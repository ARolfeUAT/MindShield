"""Tests for MindShield UI Flask Blueprint."""

def test_dashboard_get(client, mock_requests, mock_logs):
    """Tests GET /mindshield/dashboard renders dashboard with requests and logs."""
    response = client.get('/mindshield/dashboard')
    assert response.status_code == 200
    assert b'MindShield Dashboard' in response.data
    # Check mock requests are displayed
    for req in mock_requests:
        assert req['request_id'].encode() in response.data
        assert req['device_name'].encode() in response.data
        assert req['device_type'].encode() in response.data
        assert req['ipv6_address'].encode() in response.data
        assert req['status'].encode() in response.data
    # Check mock logs are displayed
    for log in mock_logs:
        assert log['log_id'].encode() in response.data
    # Check status summary
    assert b'Pending' in response.data
    assert b'Approved' in response.data
    assert b'Denied' in response.data

def test_dashboard_sort_by_timestamp(client, mock_requests):
    """Tests sorting requests by timestamp."""
    response = client.get('/mindshield/dashboard?sort=timestamp&order=desc')
    assert response.status_code == 200
    # Check order of requests (latest first)
    assert mock_requests[1]['request_id'].encode() in response.data[:response.data.find(mock_requests[0]['request_id'].encode())]

def test_dashboard_search(client, mock_requests):
    """Tests filtering requests by search query."""
    # Test with 'VR Gaming'
    response = client.get('/mindshield/dashboard?search=VR+Gaming')
    assert response.status_code == 200, f"Response status: {response.status_code}"
    assert b'req_002' in response.data, "req_002 not found in response"
    assert b'req_001' not in response.data, "req_001 should not be in response"
    assert b'req_003' not in response.data, "req_003 should not be in response"

    # Test with partial match
    response = client.get('/mindshield/dashboard?search=user_001')
    assert response.status_code == 200
    assert b'req_001' in response.data
    assert b'req_002' not in response.data
    assert b'req_003' not in response.data

    # Test with no match
    response = client.get('/mindshield/dashboard?search=nonexistent')
    assert response.status_code == 200
    assert b'req_001' not in response.data
    assert b'req_002' not in response.data
    assert b'req_003' not in response.data

def test_approve_request_post(client, mock_requests):
    """Tests POST /mindshield/approve updates request status to approved."""
    request_id = mock_requests[0]['request_id']
    response = client.post(f'/mindshield/approve/{request_id}')
    assert response.status_code == 302  # Redirect to dashboard
    # Follow redirect to verify update
    follow = client.get('/mindshield/dashboard')
    assert b'approved' in follow.data
    assert request_id.encode() in follow.data

def test_deny_request_post(client, mock_requests):
    """Tests POST /mindshield/deny updates request status to denied."""
    request_id = mock_requests[0]['request_id']
    response = client.post(f'/mindshield/deny/{request_id}')
    assert response.status_code == 302  # Redirect to dashboard
    # Follow redirect to verify update
    follow = client.get('/mindshield/dashboard')
    assert b'denied' in follow.data
    assert request_id.encode() in follow.data

def test_dashboard_404_for_invalid_route(client):
    """Tests invalid UI route returns 404."""
    response = client.get('/mindshield/invalid')
    assert response.status_code == 404