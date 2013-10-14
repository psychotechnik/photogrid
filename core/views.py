from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Chessboard


def server_error(request):
    return render(request, '500.html')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(IndexView, self).get_context_data(*args, **kwargs)
        context_data['chessboard'] = Chessboard.objects.all()[0]
        return context_data
