from django.urls import path

from my_exam_prep.expenses_tracker.views import home_page, create_expense, edit_expense, delete_expense, \
    profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', home_page, name='home page'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
    path('profile/', profile_details, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
