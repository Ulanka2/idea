from django.urls import path
from .views import idea

urlpatterns = [
    path('', idea, name='all_idea'),
]