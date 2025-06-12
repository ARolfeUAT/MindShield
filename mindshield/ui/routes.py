"""Routes for MindShield UI Flask Blueprint."""

from flask import render_template, redirect, url_for, current_app, request
import logging
import copy

from . import ui_blueprint

# Temporary logging for debugging
logging.basicConfig(level=logging.DEBUG)

@ui_blueprint.route('/dashboard')
def dashboard():
    """Renders the MindShield dashboard with access requests and logs."""
    # Deep copy to avoid modifying app config
    requests = copy.deepcopy(current_app.config.get('MOCK_REQUESTS', []))
    logs = current_app.config.get('MOCK_LOGS', [])

    # Sorting
    sort_by = request.args.get('sort', 'timestamp')
    sort_order = request.args.get('order', 'desc')
    if sort_by in ['timestamp', 'status', 'device_type']:
        reverse = sort_order == 'desc'
        requests = sorted(requests, key=lambda x: x[sort_by], reverse=reverse)

    # Filtering
    search_query = request.args.get('search', '').strip().lower()
    logging.debug(f"Search query: {search_query}")
    if search_query:
        requests = [
            req for req in requests
            if any(search_query in str(value).lower() for value in req.values())
        ]
        logging.debug(f"Filtered requests: {requests}")

    # Status summary
    status_summary = {
        'pending': sum(1 for req in requests if req['status'] == 'pending'),
        'approved': sum(1 for req in requests if req['status'] == 'approved'),
        'denied': sum(1 for req in requests if req['status'] == 'denied')
    }

    # Log final requests before rendering
    logging.debug(f"Rendering requests: {requests}")

    return render_template('dashboard.html', requests=requests, logs=logs, status_summary=status_summary)

@ui_blueprint.route('/approve/<request_id>', methods=['POST'])
def approve_request(request_id):
    """Approves an access request and updates status."""
    requests = current_app.config.get('MOCK_REQUESTS', [])
    for req in requests:
        if req['request_id'] == request_id:
            req['status'] = 'approved'
            # Update logs (in-memory for demo)
            logs = current_app.config.get('MOCK_LOGS', [])
            logs.append({
                'log_id': f'log_{len(logs) + 1:03d}',
                'request_id': request_id,
                'action': 'approved',
                'timestamp': '2025-06-10T12:02:00'  # Static for demo
            })
            current_app.config['MOCK_LOGS'] = logs
            break
    return redirect(url_for('ui.dashboard'))

@ui_blueprint.route('/deny/<request_id>', methods=['POST'])
def deny_request(request_id):
    """Denies an access request and updates status."""
    requests = current_app.config.get('MOCK_REQUESTS', [])
    for req in requests:
        if req['request_id'] == request_id:
            req['status'] = 'denied'
            # Update logs (in-memory for demo)
            logs = current_app.config.get('MOCK_LOGS', [])
            logs.append({
                'log_id': f'log_{len(logs) + 1:03d}',
                'request_id': request_id,
                'action': 'denied',
                'timestamp': '2025-06-10T12:02:00'  # Static for demo
            })
            current_app.config['MOCK_LOGS'] = logs
            break
    return redirect(url_for('ui.dashboard'))