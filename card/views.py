from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Word
from .form import WordForm


class HomeView(LoginRequiredMixin,TemplateView):
    login_url = 'user_login'
    template_name = 'home.html'


class WordCreateView(CreateView):
    model = Word
    form_class = WordForm
    template_name = 'add_word.html'  # Specify the template for rendering the form
    success_url = '/'


class WordList(ListView):
    model = Word
    template_name = "view_word.html"
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = Word.objects.all().order_by('?')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to user profile or any other page you want
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')