from django import forms

from exam.notes.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfile(ProfileForm):
    pass


class DeleteProfile(ProfileForm):
    pass


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class CreateNote(NoteForm):
    pass


class EditNote(NoteForm):
    pass


class DeleteNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
