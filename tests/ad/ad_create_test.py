import pytest


@pytest.mark.django_db
def test_ad_create(client, user, access_token):

    data = {
        "author": user.pk,
        "name": "Стол из смолы",
        "price": 200
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Стол из смолы",
        "price": 200,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": None
}
    response = client.post(
        "/ad/",
        data=data,
        HTTP_AUTHORIZATION="Bearer " + access_token)

    assert response.status_code == 201
    assert response.data == expected_data
