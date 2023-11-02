"""Views for clauses app."""

from django.http import HttpResponse


# Homempage.
def index(request):
    return HttpResponse("Hello, world. You're at the clauses index.")


# Detail for a single clause.
def detail(request, clause_id):
    return HttpResponse("You're looking at clause %s." % clause_id)


# Rating (upvotes/downvotes) for a single clause.
def rating(request, clause_id):
    response = "You're looking at the rating of clause %s."
    return HttpResponse(response % clause_id)


# Page to rate a single clause.
def rate(request, clause_id):
    return HttpResponse("You're voting on clause %s." % clause_id)
