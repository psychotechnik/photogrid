from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView

from .models import Chessboard, Photo


def server_error(request):
    return render(request, '500.html')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super(IndexView, self).get_context_data(*args, **kwargs)
        board = Chessboard.objects.all()[0]
        context_data['chessboard'] = board
        grid = []
        for row in range(8):
            row_photos = ""
            for col in range(8):
                try:
                    photo = board.photos.get(row=row, column=col)
                    row_photos += render_to_string('_photo.html', {'photo': photo, })
                except Photo.DoesNotExist:
                    row_photos += render_to_string("_square_filler.html")
            grid.append(row_photos)

        context_data['grid'] = grid

        return context_data
