from django.urls import path
from . import views

urlpatterns=[
    path('submit/expense/',views.submit_expense),
    path('submit/income/',views.submit_income),
    path('about/',views.about_view),
    path('register/',views.register),
    path('',views.home_view),

]
