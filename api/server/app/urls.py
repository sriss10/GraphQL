from django.urls import path, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from app import views
import graphql


urlpatterns=[
    path('',views.home,name='home'),
    path('gql',GraphQLView.as_view(graphiql=True)),
]