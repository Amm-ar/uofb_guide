from django.urls import path
from .views import Colleges, CollegeDetails

urlpatterns = [
    path('', Colleges.as_view()),
    path('<int:id>/', CollegeDetails.as_view()),

]
