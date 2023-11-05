from django.urls import path

from . import views

app_name = "clauses"
urlpatterns = [
    # ex: /clauses/
    path("", views.index, name="index"),
    # ex: /clauses/5/
    path("<int:clause_id>/", views.detail, name="detail"),
    # ex: /clauses/5/rate/
    path("<int:clause_id>/rate/", views.rate, name="rate"),
]
