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
                'device_name': 'Patient BCI 001',
                'device_type': 'Medical',
                'ipv6_address': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                'timestamp': '2025-06-10T12:00:00',
                'status': 'pending'
            },
            {
                'request_id': 'req_002',
                'user_id': 'user_002',
                'device_id': 'bci_002',
                'device_name': 'VR Gaming Headset',
                'device_type': 'Gaming',
                'ipv6_address': '2001:0db8:85a3:0000:0000:8a2e:0370:7335',
                'timestamp': '2025-06-10T12:01:00',
                'status': 'pending'
            },
            {
                'request_id': 'req_003',
                'user_id': 'user_003',
                'device_id': 'bci_003',
                'device_name': 'Drone Controller',
                'device_type': 'Military',
                'ipv6_address': '2001:0db8:85a3:0000:0000:8a2e:0370:7336',
                'timestamp': '2025-06-10T11:59:00',
                'status': 'approved'
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
            },
            {
                'log_id': 'log_003',
                'request_id': 'req_003',
                'action': 'approved',
                'timestamp': '2025-06-10T11:59:00'
            }
        ]
    }
