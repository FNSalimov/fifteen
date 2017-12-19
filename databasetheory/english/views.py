from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from english.models import Sphere, Word, User_Word
import json
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib import auth
from english.myforms import WordForm
from django.contrib.auth.models import User
from django.utils import timezone

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "english/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "english/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

def test(request):
    list_of_words = list(Word.objects.all())
    five_words = []
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    jsonStr = json.dumps([w.toJSON() for w in five_words])
    return HttpResponse(jsonStr, content_type='application/json')

def testt(request):
    if request.GET.get('learned') == 'true' and request.GET.get('word'):
        a = User_Word.objects.filter(user_id=auth.get_user(request),
                                word_id=Word.objects.get(title=request.GET.get('word')))
        if a:
            print('no')
        else:
            User_Word.objects.create(user_id=auth.get_user(request),
                                 word_id=Word.objects.get(title=request.GET.get('word')))
    list_of_words = list(Word.objects.all())
    random_word = list_of_words[random.randint(1, len(list_of_words) - 1)]
    jsonStr = json.dumps(random_word.toJSON())
    return HttpResponse(jsonStr, content_type='application/json')

def profile(request):
    my_words = []
    words_learned = []
    if request.user.is_authenticated():
        my_words = list(Word.objects.filter(added_by=auth.get_user(request)))
        words_learned = list(User_Word.objects.filter(user_id=auth.get_user(request)).order_by('learned_time'))
    return render(request, 'english/profile.html', {'username': auth.get_user(request).username,
                                                    'word_list': my_words,
                                                    'words_learned': words_learned})

def english(request):
    list_of_words = list(Word.objects.all())
    five_words = []
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    russian_words = five_words
    random.shuffle(five_words)
    english_words = []
    for i in range(5):
        random_number = random.randint(0, 4)
        while five_words[random_number] in english_words:
            random_number = random.randint(0, 4)
        english_words.append(five_words[random_number])
    return render(request, 'english/english.html', {'russian_words': russian_words, 'english_words': english_words, 'test': test, 'username': auth.get_user(request).username})

def index(request):
    list_of_words = list(Word.objects.all())
    return render(request, 'english/index.html', {'username': auth.get_user(request).username,
                                                'word_list': list_of_words
                                                #'spheres': spheres,
                                                #'amount': len(list_of_words)
                                                })

def add(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            Word.objects.create(title=form.cleaned_data.get('title'),
                                defenition=form.cleaned_data.get('defenition'),
                                #added_time=timezone.now(),
                                belongs=form.cleaned_data.get('belongs'),
                                added_by=auth.get_user(request))
            dd = Sphere.objects.get(title=form.cleaned_data.get('belongs').title)
            dd.amount += 1
            dd.save()
            return HttpResponseRedirect('/add')

    else:
        form = WordForm
    return render(request, 'english/add.html', {'form': form, 'username': auth.get_user(request).username})