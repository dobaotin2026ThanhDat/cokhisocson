from django.urls import path
from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('index.html', home),  # <-- thêm dòng này
]