from django.urls import path
from card.views import HomeView, WordCreateView, WordList, user_login


urlpatterns = [
 path("", HomeView.as_view(), name='home'),
 path('list', WordList.as_view(), name='list'),
 path('create/', WordCreateView.as_view(), name='create'),
 path('login/', user_login, name='user_login'),

]
