
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm, nou_usuari_form
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from .models import Usuari
from django.conf import settings
from articles.models import Article
from comandes.models import Comanda, Carret
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
                nou_carro = Carret.objects.create(usuari = nou_usuari)
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
    
    
    
def crear_admin(request, perfil_id=None):
    
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
                usuari = Usuari.objects.get( usuari = nou_usuari )
                usuari.admin = True
                usuari.save()
                nou_carro = Carret.objects.create(usuari = nou_usuari)
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
    carritu = Carret.objects.get(usuari=request.user)
    # comandes = Comanda.objects.filter(carro=carritu)
    comandes = Comanda.objects.filter(carro=carritu)
    ctx={"comandes":comandes,"carritu":carritu}
    return render(request,"menu_usuari.html",ctx)
    
    
def afegir_al_carritu(request, id_article):
    carritu = Carret.objects.get(usuari=request.user)
    article_demanat=Article.objects.get(id=id_article)
    nova_comanda = Comanda.objects.create(carro = carritu, article = article_demanat, preu = article_demanat.preu, quantitat = 1)
    carritu.preu_total += article_demanat.preu
    carritu.save()
    return redirect("usuaris:menu_usuari") 
    
def eliminar_comanda(request,id_comanda):
    comanda = Comanda.objects.get(id=id_comanda);
    carritu = Carret.objects.get(id=comanda.carro.pk)
    carritu.preu_total -= comanda.preu
    carritu.save()
    comanda.delete()
    return redirect('usuaris:menu_usuari')

def modificar_perfil(request):
    usuariForm = modelform_factory(User,fields=("first_name","last_name","email"))
    profileForm = modelform_factory(Usuari,fields=('direccio',))
    unPerfil = request.user.usuari
    unUsuari = request.user
    
    if request.method == 'POST':
        formUsuari = usuariForm(request.POST, instance = unUsuari)
        formPerfil = profileForm(request.POST, request.FILES, instance = unPerfil)
        formUsuariValid = formUsuari.is_valid()
        formPerfilValid = formPerfil.is_valid()
            
        if formUsuariValid and formPerfilValid:
            formUsuari.save()
            formPerfil.save()
            messages.info(request,"S'han modificat les dades correctament")
            return redirect('articles:index')
    else:
        formUsuari = usuariForm(instance = unUsuari)
        formPerfil = profileForm(instance = unPerfil)
        
    for f in formUsuari.fields:
       formUsuari.fields[f].widget.attrs['class'] = 'formulari'
    for f in formPerfil.fields:
       formPerfil.fields[f].widget.attrs['class'] = 'formulari'
   
    formUsuari.fields['first_name'].widget.attrs['placeholder']="Nom"
    formUsuari.fields['last_name'].widget.attrs['placeholder']="Cognoms"
    formUsuari.fields['first_name'].widget.attrs['placeholder']="email"
    formPerfil.fields['direccio'].widget.attrs['placeholder']="direccio"
    
    return render(request, 'modificar_usuari.html', {'formPerfil': formPerfil, 
                                                     'formUsuari': formUsuari } )
                                                     
                                                     
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request, id_carritu):
    preu=Carret.objects.get(id=id_carritu)
    usuari = Usuari.objects.get( usuari = request.user )
    # What you want the button to do.
    paypal_dict = {
        "business": request.user.email,
        "amount": preu.preu_total,
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "preu" : preu}
    return render(request, "payment.html", context)
    
    
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the business field request. (The user could tamper
        # with those fields on payment form before send it to PayPal)
        if ipn_obj.receiver_email != "readyspartan117@gmail.com":
            # Not a valid payment
            return redirect( 'articles:index')

        # ALSO: for the same reason, you need to check the amount
        # received etc. are all what you expect.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            #Users.objects.update(paid=True)
            eso = User.objects.get.all()
    else:
        #...
        valid_ipn_received.connect(show_me_the_money)
        
# -*- coding: utf-8 -*-


