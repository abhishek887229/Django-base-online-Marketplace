from django.urls import path
from django.contrib.auth import views as auth_views

from .import views

app_name='conversation'
urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('<int:pk>/',views.detail,name='abc'),
    path('new/<int:item_pk>/',views.new_conversation,name='new'),
]
