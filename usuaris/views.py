
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm, nou_usuari_form
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from .models import Usuari
from django.conf import settings
from articles.models import Article
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages
# Create your views here.

def crear_usuari(request, perfil_id=None):
    
    if request.method == 'POST':
        form = nou_usuari_form(request.POST )
        
        if form.is_valid():
            email = form.cleaned_data['email']
            repetit = User.objects.filter( username = email )
            #mirem si està repetit i llencem missatge error "cuidadín"
            if repetit:
                messages.error( request, "Aquest nom d'usuari ja existeix a la base de dades")
            else:
                password = form.cleaned_data['password']
                #creem el nou usuari
                nou_usuari = User.objects.create_user( username = email, email = email, password = password )
                
                messages.info(request,"Usuari creat correctament")
                return redirect('articles:index')
    else:
        form = nou_usuari_form()
    
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'formulari inputForm'
       
    form.fields['email'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['email'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'crear_usuari.html', {'form': form,} )
    
    
def login(request):

    #si tot es POST:
    if request.method=='POST':
        form=LoginForm( request.POST )

        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                               password = form.cleaned_data['password'])
               
            if user and user.is_active:
                #si tot és ok:
                authLogin( request, user )
                next = request.GET.get('next')
                messages.info(request,"Benvingut")
                return redirect(next or 'articles:index')

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
                
           
    else:
        form=LoginForm()
   
    ctx={ 'form':form, }
    form.fields['username'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['username'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'login.html', ctx )
    
def logout(request):
    authLogout( request )
    return redirect( 'articles:index')
    
    
def menu_usuari(request):
    articles_comprats= request.user.usuari.articles_comprats.all()
    
#    venuts = request.user.perfil.discos_oferta.filter(venut=True)
    ctx={"articles_comprats":articles_comprats}        
    return render(request,"menu_usuari.html",ctx)