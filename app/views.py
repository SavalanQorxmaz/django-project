from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Logo, Slider, Contacts,Photos,Projects
import base64
import io

# Create your views here.

logo = Logo.objects.all().values() or {}
contacts = Contacts.objects.all().values()

if len(logo) > 0:
   logo[0]['logo'] = str(base64.b64encode(logo[0]['logo'])).split("b'")[1].split("'")[0]

for i in contacts:
     i['contact_logo'] = str(base64.b64encode(i['contact_logo'])).split("b'")[1].split("'")[0]

def main(request):
  slider = Slider.objects.all().values()
  projects = Projects.objects.all().values()
  photos = Photos.objects.all().values()


  projectMinObject = []
  projecIdSet = set()
  mainPhotos = {}
  
 

  for slide in slider:
    slide['slide'] = str(base64.b64encode(slide['slide'])).split("b'")[1].split("'")[0]

  for i in photos:
     i['photo'] = str(base64.b64encode(i['photo'])).split("b'")[1].split("'")[0]
  
  #  i['image'] =  ImageFile(io.BytesIO(i['image']), name='test.jpg') 
    #  print(base64.b64encode(i['image']))
  # print(i['image'])
  for project in projects:
    projecIdSet.add(project['id'])
  for photo in photos:
    if ('main' in photo['photo_name'] and photo['project_id']  in projecIdSet):
      projecIdSet.remove(photo['project_id'])
      mainPhotos[str(photo['project_id'])] = photo['photo']
  for project in projects:
    index = project['id']
    projectMinObject.append({
      'id': project['id'],
      'project_name': project['name'],
      'project_text': project['Description'],
      'project_image':   mainPhotos[str(index)]  if str(index) in mainPhotos else ''
    })
    
  template = loader.get_template('index.html')
  context = {
    'logo': logo[0] if len(logo)>0 else {},
    'slider': slider,
    'projects': projectMinObject,
    'pictures': photos,
    'contacts':contacts
  }
  
  return HttpResponse(template.render(context, request))

def project(request, id):

  project = Projects.objects.get(id=id)
  photoList = Photos.objects.all().values().filter(project_id =id)
  for i in photoList:
     i['photo'] = str(base64.b64encode(i['photo'])).split("b'")[1].split("'")[0]
  template = loader.get_template('project.html')

  context = {
    'logo': logo[0] if len(logo)>0 else {},
    'project': project,
    'contacts':contacts,
    'photos':photoList
  }


  return HttpResponse(template.render(context,request))


   