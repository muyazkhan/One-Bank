from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from .forms import User_registation,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView



class UserRegistration(FormView):
    template_name = 'register.html'
    form_class = User_registation
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 

class UserLogin(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')


class UserBankAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})