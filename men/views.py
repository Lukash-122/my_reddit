from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .utils import *
from .forms import *
# Create your views here.


def QuestionHome(request):
    posts = Question.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'men/index.html', context=context)


def QuestionCategory(request, cat_slug):
    posts = Question.objects.filter(cat__slug=cat_slug)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Категорія',
        'cat_selected': cat_slug,
    }

    return render(request, 'men/index.html', context=context)


def about(request):
    return render(request, 'men/about.html', context={'title': 'Про сайт'})


# def add_question(request):
#     if request.method == "POST":
#         form = AddQuestionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('add_question')
#     form = AddQuestionForm()
#     return render(request, 'men/add_question.html', {'form': form, 'title': 'add'})


class AddQuestion(LoginRequiredMixin, CreateView):
    model = Question
    form_class = AddQuestionForm
    success_url = reverse_lazy('home')
    template_name = 'men/add_question.html'
    login_url = 'login'
    context = {'title': 'Про сайт'}
    extra_context = {'title': 'Написати питання'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def read_answer(request, question_id):
    posts = Answer.objects.filter(question_id=question_id)

    context = {
        'posts': posts,
        'title': 'Пости',
    }

    return render(request, 'men/read_answer.html', context=context)


# def write_answer(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     form = AddAnswerForm(request.POST or None, initial={'question': question})
#     if form.is_valid():
#         answer = form.save(commit=False)
#         answer.user = request.user
#         answer.question = question
#         answer.save()
#         return redirect('write_answer', question_id=question.id)
#     return render(request, 'answer.html', {'form': form})
class AddAnswer(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AddAnswerForm
    success_url = reverse_lazy('home')
    template_name = 'men/answer.html'
    login_url = 'login'
    extra_context = {'title': 'Написати відповідь'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['question_id'] = self.kwargs['question_id']
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = get_object_or_404(Question, id=self.kwargs['question_id'])
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'регістрація'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'men/login.html'
    extra_context = {'title': 'авторизація'}

    def get_success_url(self):
        return reverse_lazy('home')

