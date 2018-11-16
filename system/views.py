# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            'number': "+996 776 900 413",
            'email': "masteraalish@gmail.com"
        }


def contacts_view(request):
    context = {
        'numbers': [
            "0776900413",
            "0222900022",
            "0312333444",
            "0555200303",
        ]
    }
    return render(request, "contacts.html", context)


class SearchView(TemplateView):
    template_name = "search.html"

    def dispatch(self, request, *args, **kwargs):
        keyword = request.GET.get("keyword", None)
        context = {
            'keyword': keyword
        }
        return render(request, self.template_name, context)


class ArticlesView(TemplateView):
    template_name = "articles.html"


