from django.shortcuts import render, redirect

from my_exam_prep.expenses_tracker.forms import CreateProfile, CreateExpense, EditExpense, DeleteExpense, EditProfile, \
    DeleteProfile
from my_exam_prep.expenses_tracker.models import Profile, Expense


def home_page(req):
    profile = Profile.objects.first()
    if profile:
        expenses = Expense.objects.all()
        budget = profile.budget
        budget_left = budget - sum([x.price for x in expenses])

        context = {
            'expenses': expenses,
            'budget': budget,
            'budget_left': budget_left
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


def create_expense(req):
    if req.method == 'POST':
        form = CreateExpense(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateExpense()

    context = {
        'form': form,
    }
    return render(req, 'expense-create.html', context)


def edit_expense(req, pk):
    expense = Expense.objects.get(pk=pk)
    if req.method == 'POST':
        form = EditExpense(req.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditExpense(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(req, 'expense-edit.html', context)


def delete_expense(req, pk):
    expense = Expense.objects.get(pk=pk)
    if req.method == 'POST':
        expense.delete()
        return redirect('home page')
    else:
        form = DeleteExpense(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }
    return render(req, 'expense-delete.html', context)


def profile_details(req):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum([x.price for x in expenses])
    context = {
        'profile': profile,
        'budget_left': budget_left,
    }
    return render(req, 'profile.html', context)


def edit_profile(req):
    profile = Profile.objects.first()
    if req.method == 'POST':
        form = EditProfile(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditProfile(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(req, 'profile-edit.html', context)


def delete_profile(req):
    profile = Profile.objects.first()
    if req.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home page')
    else:
        form = DeleteProfile(instance=profile)

        context = {
            'form': form,
        }
        return render(req, 'profile-delete.html', context)
