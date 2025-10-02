from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Petition
from django.contrib.auth.decorators import login_required

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        petitions = Petition.objects.filter(name__icontains=search_term)
    else:
        petitions = Petition.objects.all()
    
    user = request.user
    for petition in petitions:
        if user.is_authenticated:
            petition.has_voted = petition.voters.filter(id=user.id).exists()
        else:
            petition.has_voted = False

    template_data = {}
    template_data['title'] = 'Petitions'
    template_data['petitions'] = petitions
    return render(request, 'petition/index.html',
                  {'template_data': template_data})

def vote(request,id):
    petition = get_object_or_404(Petition, id=id)
    user = request.user

    if not petition.voters.filter(id=user.id).exists():
        petition.voters.add(user)
        petition.votes += 1
        petition.save()
        return redirect('petition.index')
    
    return redirect('petition.index')

def unvote(request,id):
    user = request.user
    petition = get_object_or_404(Petition, id=id)

    if petition.voters.filter(id=user.id).exists():
        petition.voters.remove(user)
        petition.votes -= 1
        petition.save()
        return redirect('petition.index')
    return redirect('petition.index')

@login_required
def make_petition(request):
    if request.method == 'POST' and request.POST['comment']!= '':
        petition = Petition()
        petition.name = request.POST['comment']
        petition.user = request.user
        petition.save()
        return redirect('petition.index')
    else:
        return render(request, 'petition/make_petition.html')
    
@login_required
def delete_petition(request, id):
    petition = get_object_or_404(Petition, id=id, user=request.user)
    petition.delete()
    return redirect('petition.index')
