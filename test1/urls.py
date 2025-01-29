from . import views
from django.urls import path
# from .models import Etudiant

urlpatterns=[
   path('' , views.seeAll , name="seeAll"),
   path('add/' , views.add , name="add"),
   path('delete/<id>' , views.delete, name="delete"),
]
