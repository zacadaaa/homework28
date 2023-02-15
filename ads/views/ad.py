import json

from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ads
from homework_28 import settings
from users.models import User


class AdListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related('author').order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
                "category": ad.category_id,
            })

        response = {
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author_id,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image.url if ads.image else None,
            "category": ads.category_id,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ads
    fields = ["name", "author", "price", "description", "category"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)

        ads = Ads.objects.create(
            name=ads_data["name"],
            author_id=ads_data["author"],
            price=ads_data["price"],
            description=ads_data["description"],
            category_id=ads_data["category"]
        )

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author_id,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": ads.image.url if ads.image else None,
            "category": ads.category_id,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ads
    fields = ["name", "author", "price", "description", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        self.object.name = ads_data["name"]
        self.object.author_id = ads_data["author"]
        self.object.price = ads_data["price"]
        self.object.description = ads_data["description"]
        self.object.category_id = ads_data["category"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category": self.object.category_id,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdImageView(UpdateView):
    model = Ads
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "image": self.object.image.url if self.object.image else None,
        }
        )


class AuthorAdDetailView(View):
    def get(self, request):
        author_qs = User.objects.annotate(ad=Count('ads'))

        paginator = Paginator(author_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        authors = []
        for author in page_obj:
            authors.append({
                "id": author.id,
                "username": author.username,
                "ads": author.ad
            })

        response = {
            "items": authors,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
            "avg": author_qs.aggregate(avg=Avg('ads'))['avg']
        }

        return JsonResponse(response)
