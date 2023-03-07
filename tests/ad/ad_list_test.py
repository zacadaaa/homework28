import pytest

from tests.factories import AdFactory

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(5)

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdSerializer(ad_list, many=True).data
    }
