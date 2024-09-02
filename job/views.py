from django.shortcuts import render,get_object_or_404,redirect
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def job_list(request):

    job_list=Job.objects.all()
    paginator = Paginator(job_list, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}

    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    
    job_detail=get_object_or_404(Job,slug=slug)
    # job_detail=Job.objects.get(id=id)
    if request.method == 'POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
    else:
        form=ApplyForm()
    context={'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.owner=request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:

        form=JobForm()

    return render(request,'job/add_job.html',context={'form':form})