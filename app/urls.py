
from django.urls import path
from .views import post_create, post_delete, post_list, post_detail, post_update, like

app_name = "app"
urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create"),
    # path("<int:pk>/", post_detail, name="detail"),
    path("<str:slug>/", post_detail, name="detail"),
    # path("<int:pk>/update/", post_update, name="update"),
    path("<str:slug>/update/", post_update, name="update"),
    # path("<int:pk>/delete/", post_delete, name="delete"),
    path("<str:slug>/delete/", post_delete, name="delete"),
    path("<str:slug>/like/", like, name="like"),
]

