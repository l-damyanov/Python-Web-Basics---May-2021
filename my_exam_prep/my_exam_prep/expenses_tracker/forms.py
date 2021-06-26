from django import forms

from my_exam_prep.expenses_tracker.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfile(ProfileForm):
    pass


class EditProfile(ProfileForm):
    pass


class DeleteProfile(ProfileForm):
    pass


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class CreateExpense(ExpenseForm):
    pass


class EditExpense(ExpenseForm):
    pass


class DeleteExpense(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
