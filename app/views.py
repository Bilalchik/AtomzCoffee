from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import News
from .serializers import NewsListSerializer


class NewsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'


class NewsListView(ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsListSerializer
    pagination_class = NewsPagination




