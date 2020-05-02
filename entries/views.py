from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

class HomeView(ListView): # remove LoginRequiredMixin so that user can see homepage without login
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date'] #sorting by the item date
    paginate_by = 3 #three items per page

###readmore or full blog view
class EntryView(DetailView): # remove LoginRequiredMixin so that user can see full reading blog page without login
    model = Entry
    template_name = 'entries/entry_detail.html'

###create new post view
class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text', 'entry_image_url']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


class AboutView(ListView):
    model = Entry
    template_name = 'entries/about.html'