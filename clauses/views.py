from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the clauses index.")


def detail(request, clause_id):
    return HttpResponse("You're looking at clause %s." % clause_id)


def rating(request, clause_id):
    response = "You're looking at the rating of clause %s."
    return HttpResponse(response % clause_id)


def vote(request, clause_id):
    return HttpResponse("You're voting on clause %s." % clause_id)