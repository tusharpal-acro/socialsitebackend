from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, PostListSerializer,PostLikeSerializer
from . import models
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
import json
import requests
import datetime
from datetime import date



class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=75e84c4526414c14ab13102b77bff0c8")
        json_data=response.json()
        country_name=json_data['country']
        country_code=json_data['country_code']
        lat=json_data['latitude']
        long=json_data['longitude']
        ip=json_data['ip_address']
        day = datetime.datetime.now()
        signupday=day.strftime("%A")
        Current_Date = date.today()
        year=Current_Date.year
        month= Current_Date.month
        day= Current_Date.day
        response2 = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=47c8459efeba4150a4a9aaafb2bc984c&country={country_code}&year={year}&month={month}&day={day}")
        if len(response2.content)>3:
            li=response2.json()
            h_name=li[0]['name']
            user_obj=models.User_Detail.objects.create(user=user,country=country_name,signup_day=signupday,is_holiday=True,holiday_name=h_name,ip_address=ip,latitude=lat,longitude=long)
            user_obj.save()
        else:
            user_obj=models.User_Detail.objects.create(user=user,country=country_name,signup_day=signupday,is_holiday=False,holiday_name='None',ip_address=ip,latitude=lat,longitude=long)
            user_obj.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (permissions.IsAuthenticated, )


class LoginApi(KnoxLoginView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApi, self).post(request, format=None)


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset=models.PostLike.objects.all()
    serializer_class=PostLikeSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def create(self, request, *args, **kwargs):
        data=request.data
        data._mutable = True
        data.update({"like_user":data['like_user'] })
        obj=models.Post.objects.get(id=data['post'])
        obj.likes+=1
        obj.save()
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        data1=request.data
        data1._mutable=True
        postlike_obj=models.PostLike.objects.get(id=kwargs['pk'])
        name1=postlike_obj.like_user
        user_obj=models.User.objects.get(username=name1)
        name2=user_obj.id
        if data1['like_user']==str(name2):
            postlike_obj.delete()
            obj=models.Post.objects.get(id=data1['post'])
            obj.likes-=1
            obj.save()
        return super().update(request, *args, **kwargs)
    