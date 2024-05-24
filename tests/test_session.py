def test_one(post_etp):
    """
    Тест для POST запроса.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }
    response = post_etp(url, data)
    assert response.status_code == 201
    assert "id" in response.json()

def test_two(post_etp):
    """
    Еще один тест для POST запроса.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Another Test Post",
        "body": "This is another test post.",
        "userId": 2
    }
    response = post_etp(url, data)
    assert response.status_code == 201
    assert "id" in response.json()