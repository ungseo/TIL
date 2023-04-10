from django.urls import path
from . import views
app_name = 'eithers'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('eithers/random/', views.random, name='random'),
    path('<question_pk>/', views.detail, name='detail'),
    path('<question_pk>/comment/', views.comment, name='comment'),
]