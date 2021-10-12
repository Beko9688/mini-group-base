from django.contrib import admin
from django.urls import path
from mini_module_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('calendar/', calendar, name='calendar'),
    path('timetable/', timetable, name='timetable'),
    path('lecture/<str:subject>', lecture, name='lecture'),
    path('practice/<str:subject>', practice, name='practice'),
    path('laboratory/<str:subject>', laboratory, name='laboratory'),
    path('<int:pk>/', download, name='download'),
]
