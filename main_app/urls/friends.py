from django.urls import path, include
from ..views import friends

urlpatterns = [
    path('', friends.index, name='friends'),
    path('addfriend/<int:pk>', friends.addfriend, name='addfriend'),
]