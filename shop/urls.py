from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.courses_shop, name='courses_shop'),
    path('course/<int:course_id>', views.single_course, name='single_course'),
]
