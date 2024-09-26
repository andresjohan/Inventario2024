

from django.urls import path
from .views import CreatedResponsable

urlpatterns = [

    path('responsable/',CreatedResponsable.as_view(),name='responsable')
]
