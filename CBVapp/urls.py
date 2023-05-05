from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, PriceUpdateViewSet
# from .views import CourseListView, CourseDetailView

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/courses/price/<int:pk>', PriceUpdateViewSet.as_view())
]

# this was when we were using normal class based rest apis
# urlpatterns = [
#     path('api/courses', CourseListView.as_view()),
#     path('api/courses/<int:pk>', CourseDetailView.as_view()),
# ]
