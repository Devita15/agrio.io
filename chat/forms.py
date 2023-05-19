from django import forms
from .models import Chat,TUMOR_IMAGE,INPUT_IMAGES


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['message','receiver' ]


class TUMOR_IMAGE_FORM(forms.ModelForm):   
    class Meta: 
        model = TUMOR_IMAGE 
        fields = ['Patient_Name', 'Brain_MRI'] 


class INPUT_IMAGE_FORM(forms.ModelForm):   
    class Meta: 
        model = INPUT_IMAGES
        fields = ['Input_image'] 
