import os
from dotenv import load_dotenv

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from django.core.mail import send_mail

from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer, EmailSendSerializer

load_dotenv()

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

class SendEmailMessage(CreateAPIView):
    serializer_class = EmailSendSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = EmailSendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.data
            name = serializer.data['name']
            client_email = serializer.data['email']
            comment = serializer.data['comment']
            
            send_mail(
                f'💡 Новая заявка от {name}!',
                f"Клиент {name}, эл. почта {client_email} отправил сообщение: {comment}",
                os.environ.get("EMAIL_HOST_USER"),
                [os.environ.get("RECIPIENT_EMAIL")],
                fail_silently=False,
            )

        return Response(data={'message': 'Ваша заявка принята!'}, status=status.HTTP_200_OK)
