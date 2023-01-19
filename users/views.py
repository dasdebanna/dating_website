from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from meet.views import ProfileCreateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has bee created. you can now log in')
            return redirect('http://localhost:8000/profile/new/')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)

class ReportView( LoginRequiredMixin,CreateView):
    model = Report
    fields =['reported','reason']
    template_name = 'users/report.html'

    def form_valid(self,form):
        form.instance.reported_by = self.request.user 
        return super().form_valid(form)