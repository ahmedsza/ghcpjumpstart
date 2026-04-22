from app import app


def test_submit_feedback_success():
    client = app.test_client()

    response = client.post('/SubmitFeedback', json={
        'name': 'Alex',
        'category': 'Support',
        'message': 'Need help with my order'
    })

    assert response.status_code == 200
    assert response.get_json() == {'status': 'submitted'}


def test_submit_feedback_requires_all_fields():
    client = app.test_client()

    response = client.post('/SubmitFeedback', json={
        'name': 'Alex',
        'category': '',
        'message': 'Need help with my order'
    })

    assert response.status_code == 400
    assert response.get_json() == {'error': 'name, category and message are required'}
