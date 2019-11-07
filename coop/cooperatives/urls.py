from django.urls import path

from cooperatives.views import list_cooperatives, create_cooperative, update_cooperative, delete_cooperative

urlpatterns = [
    path('', list_cooperatives, name='list_cooperatives'),
    path('create/', create_cooperative, name='create_cooperative'),
    path('update/<str:coop_name>/', update_cooperative, name='update_cooperative'),
    path('delete/<str:coop_name>/', delete_cooperative, name='delete_cooperative'),
]
