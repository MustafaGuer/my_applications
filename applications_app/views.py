from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ApplicationItem
from .forms import UserRegistrationForm


@login_required
def home(req: HttpRequest):
    if req.method == 'POST':
        company = req.POST.get('company')
        job_title = req.POST.get('job-title')
        applied_on = req.POST.get('applied-on')

    applications = ApplicationItem.objects.filter(
        user=req.user).order_by('-id')
    context = {'applications': applications}
    return render(req, 'applications_app/crud.html', context)


def register(req: HttpRequest):
    form = UserRegistrationForm()
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(req, 'applications_app/register.html', context)
