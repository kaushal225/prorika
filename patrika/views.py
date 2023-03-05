from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProblemForm
from .models import Problem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import json
from django.http import JsonResponse
from django.contrib.auth import logout
from datetime import datetime
# Create your views here.

def get_showing_problems(request,problems):
    if request.GET and request.GET.get('filter'):
        if request.GET.get('filter') == 'complete':
            return problems.filter(is_completed=True)
        if request.GET.get('filter') == 'incomplete':
            return problems.filter(is_completed=False)
    return problems

@login_required(login_url='auth/registration')
def index(request):
    problems=Problem.objects.filter(owner=request.user)
    print(problems)
    completed_count=problems.filter(is_completed=True).count()
    incompleted_count=problems.filter(is_completed=False).count()
    all_count=problems.count()
    context={'problems':get_showing_problems(request,problems),'all_count':all_count,'completed_count':completed_count,'incompleted_count':incompleted_count}

    return render(request,'patrika/index.html',context)

@login_required(login_url='auth/login')
def create_problem(request):
    form=ProblemForm()
    context={'form':form}

    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        is_completed = request.POST.get('is_completed',False)
        website=request.POST.get('website')
        problem=Problem()
        problem.name=name
        problem.description=description
        problem.is_completed= True if is_completed=='on' else False
        problem.owner=request.user
        problem.website=website
        problem.created_at=datetime.now()
        problem.save()
        messages.add_message(request,messages.SUCCESS,'problem added successfully')

        return HttpResponseRedirect(reverse("problem",kwargs={'id':problem.pk}))


    return render(request,'patrika/create-journal.html',context)
login_required(login_url='auth/login')
def problem_detail(request,id):
    
    problem=get_object_or_404(Problem,pk=id)
    problems=Problem.objects.filter(owner=request.user)
    if(problem.owner!=request.user):
        messages.error(request,'beware you are trying to access someone else\'s data ')
        logout(request)
        return redirect('home')
    return render(request,'patrika/journal-detail.html',{'problem':problem,'problems':problems})

def problem_delete(request,id):
    problem=get_object_or_404(Problem,pk=id)
    if request.method == 'POST':
        problem.delete()
        messages.add_message(request,messages.SUCCESS,'problem deleted successfully')
        return HttpResponseRedirect(reverse('home'))
    return render(request,'patrika/delete-journal.html',{'problem':problem})


def problem_update(request,id):
    problem=get_object_or_404(Problem,pk=id)
    form=ProblemForm(instance=problem)
    context={'form':form,'problem':problem}
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        is_completed = request.POST.get('is_completed',False)
        website=request.POST.get('website')

        problem.name=name
        problem.description=description
        problem.is_completed= True if is_completed=='on' else False
        problem.website=website
        problem.save()

        messages.add_message(request,messages.SUCCESS,'problem updated successfully')
        return HttpResponseRedirect(reverse("problem",kwargs={'id':problem.pk}))
    
    return render(request,'patrika/update-journal.html',context=context)




def search_problems(request):
    if request.method=='POST':
        search_text=json.loads(request.body).get('search_text')
        problems=Problem.objects.filter(website__icontains=search_text,owner=request.user) or Problem.objects.filter(name__icontains=search_text,owner=request.user)
        return JsonResponse(list(problems.values()),safe=False)