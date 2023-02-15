import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView

from users.models import Location


class LocListView(ListView):
    model = Location

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for loc in self.object_list:
            response.append({
                "id": loc.id,
                "name": loc.name,
                "lat": loc.lat,
                "lng": loc.lng,
            })
        return JsonResponse(response, safe=False)


class LocDetailView(DetailView):
    model = Location

    def get(self, request, *args, **kwargs):
        loc = self.get_object()

        return JsonResponse({
                "id": loc.id,
                "name": loc.name,
                "lat": loc.lat,
                "lng": loc.lng,
        })


@method_decorator(csrf_exempt, name="dispatch")
class LocCreateView(CreateView):
    model = Location
    fields = ["name", "lat", "lng"]

    def post(self, request, *args, **kwargs):
        loc_data = json.loads(request.body)

        loc = Location.objects.create(
            name=loc_data["name"],
            lat=loc_data["lat"],
            lng=loc_data["lng"],
        )

        return JsonResponse({
                "id": loc.id,
                "name": loc.name,
                "lat": loc.lat,
                "lng": loc.lng,
        })


@method_decorator(csrf_exempt, name="dispatch")
class LocDeleteView(DeleteView):
    model = Location
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)