from django.views.generic import ListView

from book.models import Book


class HomeView(ListView):
    template_name = 'index.html'

    queryset = Book.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data()
        print(context)
        return context
