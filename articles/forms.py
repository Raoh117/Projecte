from django import forms


class ArticleForm (forms.Form):
    imatge = forms.ImageField(label='Selecciona un archivo')
    nom = forms.CharField(max_length=120, label = 'nom')
    consola = forms.CharField(max_length=120,label="consola")
    companyia = forms.CharField(max_length=120,label="companyia")
    stock = forms.IntegerField(label ="stock")
    PEGI_CHOICES = (
                        ( '3', '3'),
                        ( '7', '7'),
                        ( '12', '12'),
                        ( '16', '16'),
                        ( '18', '18'),
                    )
    PEGI=forms.CharField(label="PEGI",max_length=50,widget=forms.Select(choices=PEGI_CHOICES),)
    preu=forms.IntegerField(label="preu")
    detalls= forms.CharField(label="detalls",widget=forms.Textarea)
    
    COL_CHOICES = (
                        ( 'Coleccionista', 'Coleccionista'),
                        ( 'Normal', 'Normal'),
                    )
    coleccionista=forms.CharField(label="coleccionista",max_length=50,widget=forms.Select(choices=COL_CHOICES),)
    
