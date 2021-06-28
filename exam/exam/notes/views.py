from django.shortcuts import render, redirect

from exam.notes.forms import CreateProfile, CreateNote, EditNote, DeleteNote, DeleteProfile
from exam.notes.models import Profile, Note


def index(req):
    profile = Profile.objects.first()
    if profile:
        notes = Note.objects.all()
        context = {
            'profile': profile,
            'notes': notes,
        }
        return render(req, 'home-with-profile.html', context)
    else:
        if req.method == 'POST':
            form = CreateProfile(req.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = CreateProfile()

        context = {
            'form': form,
        }

        return render(req, 'home-no-profile.html', context)


def create_note(req):
    if req.method == 'POST':
        form = CreateNote(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNote()

    context = {
        'form': form,
    }
    return render(req, 'note-create.html', context)


def edit_note(req, pk):
    note = Note.objects.get(pk=pk)
    if req.method == 'POST':
        form = EditNote(req.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNote(instance=note)

    context = {
        'form': form,
    }
    return render(req, 'note-edit.html', context)


def delete_note(req, pk):
    note = Note.objects.get(pk=pk)
    if req.method == 'POST':
        note.delete()
        return redirect('home page')
    else:
        form = DeleteNote(instance=note)

    context = {
        'form': form,
    }
    return render(req, 'note-delete.html', context)


def details_note(req, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(req, 'note-details.html', context)


def profile_page(req):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes_count = len(notes)
    context = {
        'profile': profile,
        'notes': notes,
        'notes_count': notes_count,
    }
    return render(req, 'profile.html', context)


def delete_profile(req, pk):
    profile = Profile.objects.get(pk=pk)
    profile.delete()
    Note.objects.all().delete()
    return redirect('home page')
