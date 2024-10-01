from django.urls import path
import blog.views

urlpatterns = [
    path('<slug:slug>/', blog.views.post_detail, name='post_detail'),
]
