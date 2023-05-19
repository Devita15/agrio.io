from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 

from chat.forms import *

import TESTING_CNN


class HomePage(TemplateView):
	template_name = 'index.html'


def DETECTION_PAGE(request):   
    if request.method == 'POST': 
        form = INPUT_IMAGE_FORM(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('display_result') 
    else: 
        form = INPUT_IMAGE_FORM() 
    return render(request, 'detection.html', {'form' : form}) 
  


def display_result(request):   
        IMAGES = INPUT_IMAGES.objects.all()
        print(IMAGES[len(IMAGES)-1].Input_image )
        print('./' + str(IMAGES[len(IMAGES)-1].Input_image ))
        result, accuracy, time2execute,precautionary_measure = TESTING_CNN.get('./' + str(IMAGES[len(IMAGES)-1].Input_image ))
        return render(request, 'display_result.html', {'input_image':IMAGES[len(IMAGES)-1].Input_image,'result':result,'accuracy':accuracy,'time2execute':time2execute,'precautionary_measure':precautionary_measure })



def feedback(request):   
    if request.method == 'POST': 
        return render(request, 'feedback.html',{'fb':'Feedback submitted successfully !'}) 
    else:
        return render(request, 'feedback.html') 
    





#crop_names = ['Mango',
#'Orange',
#'Watermelon',
#]



#crop_description = ['Mangoes are a fruit that is part of the drupe family. Mangoes have a thin, waxy, red and green skin that covers the outside. Inside, there is a large pit in the middle of the bright orange flesh. Mangoes have a sweet, tangy flavor.',
#'An orange is a fruit of various citrus species in the family Rutaceae (see list of plants known as orange); it primarily refers to Citrus × sinensis, which is also called sweet orange, to distinguish it from the related Citrus × aurantium, referred to as bitter orange.',
#'Watermelon is grown in favorable climates from tropical to temperate regions worldwide for its large edible fruit, which is a berry with a hard rind and no internal divisions, and is botanically called a pepo. The sweet, juicy flesh is usually deep red to pink, with many black seeds, although seedless varieties exist.',

#]


#res = dict(zip(crop_names, crop_description))

#def crop_description(request):   
#    if request.method == 'POST': 
 #       description =request.POST['sys']
 #       description_of_crop = res[description]
  #      return render(request, 'crop_description.html',{'description_of_crop':description_of_crop,'description':description}) 
  #  else:
   #     return render(request, 'crop_description.html',{'crop_names':crop_names}) 


from django.shortcuts import render, redirect

from django.shortcuts import render

from django.shortcuts import render, redirect

crop_array = [
    {
        'name': 'Mango',
        'description': 'Mangoes are a fruit...',
        'image_url': 'static\BG2.jpg'
    },
    {
        'name': 'Orange',
        'description': 'An orange is a fruit...',
        'image_url': 'static\logo.png'
    },
    {
        'name': 'Watermelon',
        'description': 'Watermelon is grown...',
        'image_url': 'static\BG2.jpg'
    }
]

def crop_description(request):
    if request.method == 'GET':
        return render(request, 'crop_description.html', {'crop_array': crop_array})
        # # crop_name = request.GET.get('crop_name')
        # if crop_name:
        #     crop = next((crop for crop in crop_description if crop['name'] == crop_name), None)
        #     if crop:
        #         return render(request, 'crop_details.html', {'crop': crop})
        # return render(request, 'crop_description.html', {'crop_description': crop_description})

def crop_details(request, crop_name):
    crop = next((crop for crop in crop_description if crop['name'] == crop_name), None)
    if crop:
        return render(request, 'crop_details.html', {'crop': crop})
    else:
        return redirect('crop_description')





disease_names = ['Black_rot',
'ESCA',
'Leaf_blight'
]

disease_description = [" Black rot is a potentially lethal bacterial disease that affects cruciferous vegetables such as broccoli, Brussels sprouts, cabbage, cauliflower, kale, rutabaga and turnip, as well as cruciferous weeds such as shepherd's purse and wild mustard.",
"Esca is a grape disease of mature grapevines. It is a type of grapevine trunk disease. The fungi Phaeoacremonium aleophilum, Phaeomoniella chlamydospora and Fomitiporia mediterranea are associated with the disease.",
'Grape leaf blight is caused by the fungus Phakopsora euvitis and mainly occurs in warm temperate and subtropical grape growing regions. Grapevine leaf rust only infects grapes, usually affecting leaves but can also damage fruit and stems, resulting in damage to grape crops.'
]

disease_res = dict(zip(disease_names, disease_description))

def disease_description(request):   
    if request.method == 'POST': 
        description =request.POST['sys']
        description_of_crop = disease_res[description]
        return render(request, 'disease_description.html',{'description_of_crop':description_of_crop,'description':description}) 
    else:
        return render(request, 'disease_description.html',{'crop_names':disease_names}) 


