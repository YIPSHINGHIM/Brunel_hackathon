from django.http import JsonResponse
from django.shortcuts import render


def getRoutes(request):

    list = [1,2,3,4,5,6,7,8,10]

    return JsonResponse(list,safe=False)

