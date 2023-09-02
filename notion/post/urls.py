from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/create_sub_post/', views.create_sub_post, name='create_sub_post'),
    path('pages/', views.PageListCreateAPIView.as_view(), name='page-list-create'),
    path('pages/<int:pk>/', views.PageDetailAPIView.as_view(), name='page-detail'),
    path('pages/<int:parent_page_id>/subpages/', views.SubPageCreateAPIView.as_view(), name='subpage-create'),

]
