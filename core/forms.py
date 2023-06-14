from django import forms
from django.forms import ModelForm
from core.models import IQ_Test, EQ_Test

class IQ_Test_Form(ModelForm):
    class Meta:
        model=IQ_Test
        fields=["score"]
        widgets={"score":forms.NumberInput(attrs={"min":0,"max":50})}
        labels={"score":"Введите свои баллы в форму ниже"}
        
class EQ_Test_Form(ModelForm):
    class Meta:
        model=EQ_Test
        fields=["result"]
        widgets={"result":forms.TextInput()}
        labels={"result":"Введите свои ответы в форму ниже"}
        
