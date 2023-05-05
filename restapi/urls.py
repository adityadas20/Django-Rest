from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees', views.employeeListView),
    path('api/employees/<int:pk>', views.employeeDetailView),
    path('api/users', views.userListView),
    path('', include('CBVapp.urls'))
]
