from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ads
from ads.permissions import IsOwner, IsStaff
from ads.serializers import AdSerializer


class AdListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        ad_text = request.GET.get('name')
        if ad_text:
            self.queryset = self.queryset.filter(name__icontains=ad_text)

        location_text = request.GET.get('location')
        if location_text:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location_text)

        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=int(price_from))
        if price_to:
            self.queryset = self.queryset.filter(price__lte=int(price_to))

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsStaff]


class AdDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsStaff]
