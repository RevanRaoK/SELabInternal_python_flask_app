from app import app


def test_index_status_and_body():
    app.config['TESTING'] = True
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello, World!' in resp.data
