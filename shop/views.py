from django.shortcuts import render
from django.views.generic import CreateView
from .models import User, Product
from .forms import RegisterForm, LoginForm
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'temps/register.html'
    success_url = reverse_lazy('shop:login')


class Login(FormView):
    template_name = 'temps/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Неправильное имя пользователя или пароль.')
            return self.form_invalid(form)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('shop:index')
    else:
        return redirect('shop:login')


class UserProfileListView(generic.ListView):
    model = User
    template_name = 'temps/profile.html'


def catalog(request):
    products = Product.objects.all()
    return render(request, "temps/catalog.html", {"products": products})