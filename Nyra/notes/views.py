from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("read_note")
    else:
        form = NoteForm()

    return render(request, "create_note.html", {"form": form})


def read_note(request):
    # Recupera todas as notas do banco de dados, ordenadas pela data de atualização
    notes = Note.objects.all()

    # Renderiza o template com a lista de notas
    return render(request, "read_note.html", {"notes": notes})


def update_note(request):
    model = Note
    fields = ["title", "text"]
    # template_name_suffix =
