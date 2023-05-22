from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer


class NewsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class NewsListView(ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsListSerializer
    pagination_class = NewsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_coffee']


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


