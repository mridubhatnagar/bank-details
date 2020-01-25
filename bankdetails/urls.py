from django.urls import path, include
from bankdetails import views

urlpatterns = [
    path('banks/<str:pk>/', views.BankDetail.as_view()),
    path('branchdetail', views.BranchDetail.as_view()),
    
]