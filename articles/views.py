from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from articles.models import Article
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.



def index(request):
    articles= Article.objects.all();
    ctx={'llista_articles': articles}
    return render(request, "articles/index.html",ctx)
    
def article(request,id_article):
    article = get_object_or_404(Article,pk=id_article)
    ctx={'article': article}
    return render(request,"articles/article.html",ctx)
    
def crear_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        
        if form.is_valid():
           nom= form.cleaned_data['nom']
           consola = form.cleaned_data['consola']
           PEGI=form.cleaned_data['PEGI']
           stock=form.cleaned_data['stock']
           companyia=form.cleaned_data['companyia']
           preu=form.cleaned_data['preu']
           coleccionista=form.cleaned_data['coleccionista']
           detalls=form.cleaned_data['detalls']
           imatge=form.cleaned_data['imatge']
           #creem l'objecte OFERTA_DISC amb les dades rebudes
           Article.objects.create( nom=nom,
                                        consola=consola,
                                        PEGI=PEGI,
                                        stock=stock,
                                        companyia=companyia,
                                        preu=preu,
                                        coleccionista=coleccionista,
                                        detalls=detalls,
                                        imatge=imatge,)   
           messages.info(request,"joc pujat correctament")
           return redirect("usuaris:menu_usuari")    
    else:
        form= ArticleForm()
        
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'formulari'
        
    return render (request, 'articles/crear_article.html', {'form': form} )   
    
    
def eliminar_article(request,id_article=None):
    
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id_article);
        if (id_article):
            article.delete()
            return redirect('usuaris:menu_usuari')
    else:
        return render(request, 'articles/eliminar_article.html', {'Article': Article.objects.get(pk=id_article)})
        
def cercador(request):
    #fem la consulta
    query = request.GET.get('q', '')
    tipus= request.GET.get('tipus_de_recerca')
    
    if query:
        if tipus == "titol":
            query.delete
            #discos
            #q_consulta = Q(titol__icontains = query )
        elif tipus == "grup":
            query.delete
            #grup
            #q_consulta = Q(grup__icontains = query )
        elif tipus == "genere":
            query.delete
            #genere
            #q_consulta = Q(genere__icontains = query )
        #resultats me'ls fiques a la variable 'results'    
        results = Article.objects.filter()
    else:
        results = [] #que no aparegui res
        
    return render( request, "articles/index.html", 
                                { "llista_articles": results,
                                   "query": query }
                               )