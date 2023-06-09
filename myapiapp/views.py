from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Number

@csrf_exempt
def create_number(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        description = request.POST.get('description')
        category = request.POST.get('category')
        number = Number.objects.create(value=value, description=description, category=category)
        return JsonResponse({'message': 'Number created successfully', 'number_id': number.id})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

def get_all_numbers(request):
    numbers = Number.objects.all()
    data = [{'value': number.value, 'description': number.description, 'category': number.category} for number in numbers]
    return JsonResponse({'numbers': data})

def get_number(request, number_id):
    try:
        number = Number.objects.get(id=number_id)
        data = {'value': number.value, 'description': number.description, 'category': number.category}
        return JsonResponse(data)
    except Number.DoesNotExist:
        return JsonResponse({'message': 'Number not found'}, status=404)

@csrf_exempt
def update_number(request, number_id):
    try:
        number = Number.objects.get(id=number_id)
        if request.method == 'PUT' or request.method == 'PATCH':
            number.value = request.POST.get('value', number.value)
            number.description = request.POST.get('description', number.description)
            number.category = request.POST.get('category', number.category)
            number.save()
            return JsonResponse({'message': 'Number





