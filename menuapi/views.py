from django.shortcuts import render
from rest_framework.views import APIView
from menuapi.serializers import MenuSerializers
from rest_framework.response import Response
from rest_framework import status
from menuapi.models import CoursesOfMeals
from rest_framework import viewsets


# Create your views here.

class FoodView(APIView):
    def get(self,request,*args,**kwargs):
        food=CoursesOfMeals.objects.all()
        serializer=MenuSerializers(food,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serialzers=MenuSerializers(data=request.data)
        if serialzers.is_valid():
            serialzers.save()
            return Response(serialzers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialzers.errors,status=status.HTTP_400_BAD_REQUEST)

class MenuDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        food=CoursesOfMeals.objects.get(id=id)
        serializer=MenuSerializers(food)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        food=CoursesOfMeals.objects.get(id=id)
        serialzers=MenuSerializers(instance=food,data=request.data)
        if serialzers.is_valid():
            serialzers.save()
            return Response(serialzers.data,status=status.HTTP_200_OK)
        else:
            return Response(serialzers.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        food=CoursesOfMeals.objects.get(id=id)
        food.delete()
        return Response({"message":"deleted"},status=status.HTTP_200_OK)