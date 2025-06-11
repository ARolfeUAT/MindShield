"""Routes for MindShield UI Flask Blueprint."""

from flask import render_template, redirect, url_for, current_app

from . import ui_blueprint


@ui_blueprint.route('/dashboard')
def dashboard():
    """Renders the MindShield dashboard with access requests and logs."""
    requests = current_app.config.get('MOCK_REQUESTS', [])
    logs = current_app.config.get('MOCK_LOGS', [])
    return render_template('dashboard.html', requests=requests, logs=logs)


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
