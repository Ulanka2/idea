from django.urls import path
from idea import views

urlpatterns = [
    path('', views.idea, name='idea'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('add/', views.add_idea, name='add_idea'),
    path('<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('tag/<int:pk>/', views.tag_detail_view, name='news_by_tag'),
    path('tag/create/', views.create_author, name='create_author')
]