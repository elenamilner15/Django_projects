from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Profile
import json

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        
        if name and email:
            profile = Profile.objects.create(name=name, email=email)
            return JsonResponse({'message': 'Profile created successfully'})
        else:
            return JsonResponse({'error': 'Name and email are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)




@csrf_exempt
def delete_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return JsonResponse({'message': 'Profile deleted successfully'})