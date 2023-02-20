from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from ads.models import Categories
from ads.serializers import CategoriesSerializer


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, safe=False)


class CatViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
