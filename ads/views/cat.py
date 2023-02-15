import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView

from ads.models import Categories


def index(request):
    response = {"status": "ok"}
    return JsonResponse(response, safe=False)


class CategoriesListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesCreateView(CreateView):
    model = Categories
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        categories_data = json.loads(request.body)

        categories = Categories.objects.create(
            name=categories_data["name"]
        )

        return JsonResponse({
            "id": categories.id,
            "name": categories.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

