from django.urls import path
from . import views

app_name = "to_do_app"

urlpatterns = [
    path('', views.index, name="index"),
    # path('profile/', views.profile, name="profile"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('add_task/', views.add_task, name="add_task"),
    path('done/<int:id>', views.done, name="done"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),

]