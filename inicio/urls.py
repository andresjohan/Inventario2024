

from django.urls import path
from .views import index,CreatedResponsable

urlpatterns = [
    path('',index,name='index'),
    path('responsable/',CreatedResponsable.as_view(),name='responsable')
]
