import pytest


@pytest.mark.django_db
def test_create_ad(client, token, user):
    request_data = {
        "name": "name for test",
        "price": 100,
    }

    expected_data = {
            "id": 1,
            "name": "name for test",
            "author": None,
            "price": 100,
            "description": None,
            "is_published": False,
            "image": None,
            "category": None
    }
    response = client.post(
        "/ad/create/",
        request_data,
        HTTP_AUTHORIZATION="Bearer " + token
    )
    assert response.status_code == 201
    assert response.data == expected_data
