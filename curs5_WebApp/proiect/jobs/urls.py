from django.urls import path

from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.ListJobsView.as_view(), name='list'),
    path('create/', views.CreateJobView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateJobView.as_view(), name='update'),
    path('delete/<int:pk>/', views.delete_job, name='remove'),
]
