# Adapte conforme suas necessidades
from django.urls import path
from .views import create_note, list_note

urlpatterns = [
    path("create/>", create_note, name="create_note"),  # create
    path("list/<int:pk>", list_note, name="list_note"),  # read
    # update
    # delete
]
