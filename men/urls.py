from django.urls import path
from django.views.decorators.cache import cache_page


from .views import *

urlpatterns = [
    path('', QuestionHome, name='home'),
    path('about', about, name='about'),
    path('add_question', AddQuestion.as_view(), name='add_question'),
    path('category/<slug:cat_slug>/', QuestionCategory, name='category'),
    path('read_answer/<int:question_id>/', read_answer, name='read_answer'),
    path('write_answer/<int:question_id>/', AddAnswer.as_view(), name='write_answer'),
    path('logout', logout_user, name='logout'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
]
