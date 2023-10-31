from django.urls import path

from . import views

urlpatterns = [
    # ex: /clauses/
    path("", views.index, name="index"),
    # ex: /clauses/5/
    path("<int:clause_id>/", views.detail, name="detail"),
    # ex: /clauses/5/results/
    path("<int:clause_id>/rating/", views.rating, name="rating"),
    # ex: /clauses/5/vote/
    path("<int:clause_id>/vote/", views.vote, name="vote"),
]
