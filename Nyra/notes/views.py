from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import NoteForm
from .models import Note


class NoteCreateView(CreateView):
    model = Note
    template_name = "components/create_note.html"
    context_object_name = "note"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class NoteDetailView(DetailView):
    model = Note
    template_name = "components/detail.html"
    context_object_name = "note"


class NoteUpdateView(UpdateView):
    model = Note
    template_name = "components/update.html"
    context_object_name = "note"
    form_class = NoteForm
    success_url = reverse_lazy("home_page")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "components/delete.html"
    context_object_name = "note"
    success_url = reverse_lazy("home_page")


class NoteListView(ListView):
    model = Note
    template_name = "notes/index.html"
    context_object_name = "note"
    ordering = ["-created_at"]
