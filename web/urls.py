from django.urls import path
from web.views import about, contact, detall, hospi, index, user

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('hospi/', hospi, name='hospi'),
    path('user/', user, name='user'),
    path('detall/<int:id>', detall, name='detall'),
]
