from django.urls import path
from .views import home, about, listAssurance, assurance_details, new_assurance,edit_assurance,delete_assurance

urlpatterns=[
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("listAssurance/", listAssurance, name="listAssurance" ),
    path("listAssurance/<int:id>/", assurance_details, name="details"),
    path("listAssurance/new/", new_assurance, name="new_assurance" ),
    path("listAssurance/edit/<int:id>/", edit_assurance, name="edit_assurance"),
    path("listAssurance/delete/<int:id>/", delete_assurance, name="delete_assurance")
]