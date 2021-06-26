from django.contrib import admin

from my_exam_prep.expenses_tracker.models import Profile, Expense

admin.site.register(Profile)
admin.site.register(Expense)
