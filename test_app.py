from app import app


def test_index_renders_contact_form():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'id="contactForm"' in html
    assert 'name="name"' in html
    assert 'name="category"' in html
    assert 'name="message"' in html


def test_index_includes_submit_feedback_script():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert 'function SubmitFeedback(feedback)' in response.get_data(as_text=True)
