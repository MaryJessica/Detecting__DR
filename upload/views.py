from django.shortcuts import render, redirect
import cloudinary.uploader
import cloudinary
import requests
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
cloudinary.config(cloud_name='dmryltnrf', api_key='436999286379359',
                  api_secret='0YlfKhw0YauvpE12iU2qHxbBpZ0')


def drdetection(request):
    url12 = None
   
    if request.POST:
        return _extracted_from_drdetection_10(request, url12)
    
    return render(request, 'fileupload.html')


def _extracted_from_drdetection_10(request, url12):
    file = request.FILES['files']
    upload_result = cloudinary.uploader.upload(file)
    url = upload_result['url']
    URL = 'https://diabetic-retinopathy-api.herokuapp.com/?link=' + url
    response = requests.get(URL)
    data = response.json()
    print(data["predict"])
    context = {
        'proimage': url12,
        'predict': data["predict"],
        'url': url,
        'pagetitle': 'DR prediction',
    }
    return render(request, 'prediction.html', context)


def user_home(request):
    return render(request,'home.html',{})