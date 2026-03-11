from django.http import JsonResponse
from django.shortcuts import render
from core.models import Testing
from core.serializers import TestingSerializer

def testing_view(request):
    testings = Testing.objects.all()
    serializer = TestingSerializer(testings, many=True)
    return JsonResponse(serializer.data, safe=False)

def health_check(request):
    return JsonResponse({'status': 'ok'})

def testing_detail_view(request, id):        # 👈 add this
    try:
        testing = Testing.objects.get(id=id)
        serializer = TestingSerializer(testing)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)