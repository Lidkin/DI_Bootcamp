from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
import json

# Create your views here.
@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        profile_data = json.loads(request.body)
        profile = Profile.objects.create(
                name=profile_data.get('name'),
                email=profile_data.get('email'),
                is_active=profile_data.get('is_active', True)
            )
        profile_dict = {
                'id': profile.id,
                'name': profile.name,
                'email': profile.email,
                'is_active': profile.is_active
        }
        return JsonResponse({'profile': profile_dict}, status=201)       


@csrf_exempt
def delete_profile(request, id):
    if request.method =='DELETE':
        try:
            profile = Profile.objects.get(id=id)
            profile.delete()
            return JsonResponse({'message': 'Profile deleted successfully'}, status=204)
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'profile not found'}, status=404)

def list_profiles(request):
    profiles = Profile.objects.all()
    profiles_data = [{'id': profile.id, 'name': profile.name, 'email': profile.email, 'is_active': profile.is_active} for profile in profiles]
    return JsonResponse({'profiles': profiles_data})

                