from django.contrib import admin
from django.urls import include, path
from backend.api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('api/v1/tasks', views.get_all_tasks, name='get_all_tasks'),
    path('api/v1/tasks/<int:id>', views.get_task,name='get_task'),
    path('api/v1/tasks/add', views.add_task,name='add_task'),
    path('api/v1/tasks/<int:id>/delete', views.delete_task,name='delete_task'),
    path('api/v1/tasks/<int:id>/update', views.update_task,name='update_task'),
    path('api/v1/tasks/search/<str:term>', views.search_task,name='search_task'),
]