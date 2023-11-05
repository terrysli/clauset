"""Views for clauses app."""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Clause, Rating


# Homempage.
def index(request):
    latest_clause_list = Clause.objects.order_by("-pub_date")[:5]
    context = {"latest_clause_list": latest_clause_list}
    return render(request, "clauses/index.html", context)


# Detail for a single clause.
def detail(request, clause_id):
    clause = get_object_or_404(Clause, pk=clause_id)
    return render(request, "clauses/detail.html", {"clause": clause})


# Submit a rating for a single clause.
def rate(request, clause_id):
    clause = get_object_or_404(Clause, pk=clause_id)

    try:
        rating = request.POST["rating"]
    except (KeyError, Clause.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "clauses/detail.html",
            {
                "rating": rating,
                "error_message": "You didn't select a rating.",
            },
        )
    else:
        rating.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("clauses:results", args=(clause.id,)))