"""Views for clauses app."""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Clause


# Homempage.
def index(request):
    latest_clause_list = Clause.objects.order_by("-pub_date")[:5]
    context = {"latest_clause_list": latest_clause_list}
    return render(request, "clauses/index.html", context)


# Detail for a single clause.
def detail(request, clause_id):
    clause = get_object_or_404(Clause, pk=clause_id)
    return render(request, "clauses/detail.html", {"clause": clause})


# Rating (upvotes/downvotes) for a single clause.
def rating(request, clause_id):
    response = "You're looking at the rating of clause %s."
    return HttpResponse(response % clause_id)


# Page to rate a single clause.
def rate(request, clause_id):
    return HttpResponse("You're voting on clause %s." % clause_id)
