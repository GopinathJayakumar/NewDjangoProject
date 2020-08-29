from django.urls import path
from .views import chat_details_view, chat_list_view

urlpatterns = [
    path('', chat_details_view, name='details_view'),
    path('1/', chat_list_view, name='list_view'),
]