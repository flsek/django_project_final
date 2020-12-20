from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
# Create your views here.
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'
class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

def update(request, bookmark_id):
    return render(request, 'bookmark/bookmark_update.html', {'bookmark': bookmark_id})

def delete(request, bookmark_id):
    return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark_id})
