"""Generates mock data for MindShield UI testing."""


def generate_mock_data():
    """Generates mock access requests and logs.

    Returns:
        dict: Contains lists of requests and logs.
    """
    return {
        'requests': [
            {
                'request_id': 'req_001',
                'user_id': 'user_001',
                'device_id': 'bci_001',
                'timestamp': '2025-06-10T12:00:00',
                'status': 'pending'
            },
            {
                'request_id': 'req_002',
                'user_id': 'user_002',
                'device_id': 'bci_002',
                'timestamp': '2025-06-10T12:01:00',
                'status': 'pending'
            }
        ],
        'logs': [
            {
                'log_id': 'log_001',
                'request_id': 'req_001',
                'action': 'requested',
                'timestamp': '2025-06-10T12:00:00'
            },
            {
                'log_id': 'log_002',
                'request_id': 'req_002',
                'action': 'requested',
                'timestamp': '2025-06-10T12:01:00'
            }
        ]
    }
