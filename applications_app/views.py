from datetime import date, datetime
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import ApplicationItem
from .forms import UserRegistrationForm


@login_required
def home(req: HttpRequest):
    if req.method == 'POST':
        company = req.POST.get('company')
        job_title = req.POST.get('job-title')
        applied_on = req.POST.get('applied-on')
        applied_on_date_obj = datetime.strptime(applied_on, '%Y-%m-%d')
        get_an_invitation = bool(req.POST.get('get-invitation'))
        application = ApplicationItem.objects.create(
            company=company, job_title=job_title, get_an_invitation=get_an_invitation, applied_on=applied_on, user=req.user)
        return redirect('home')

    applications = ApplicationItem.objects.filter(
        is_completed=False, user=req.user).order_by('-id')

    paginator = Paginator(applications, 4)

    page_number = req.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {'applications': applications, 'page_obj': page_obj}

    return render(req, 'applications_app/crud.html', context)


def update_application(req: HttpRequest, pk):
    application = get_object_or_404(ApplicationItem, id=pk, user=req.user)
    application.company = req.POST.get(f"application_company_{pk}")
    application.job_title = req.POST.get(f"application_job_{pk}")
    application.applied_on = req.POST.get(f"application_date_{pk}")
    application.get_an_invitation = bool(
        req.POST.get(f"application_invited_{pk}"))
    application.save()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


def delete_application(req: HttpRequest, pk):
    application = get_object_or_404(ApplicationItem, id=pk, user=req.user)
    application.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


def complete_application(req: HttpRequest, pk):
    application = get_object_or_404(ApplicationItem, id=pk, user=req.user)
    application.is_completed = True
    application.save()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


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
