# Django Imports
from django.urls import path

# In App Imports
from MainApp.views import CSVFileCreateView, CSVFileDetailView, CSVFileListView


app_name = 'MainApp'

urlpatterns = [
    path('csvfile/list', CSVFileListView.as_view(), name='csvfile_list'),
    path('csvfile/create', CSVFileCreateView.as_view(), name='csvfile_create'),
    path('csvfile/<int:pk>/detail', CSVFileDetailView.as_view(), name='csvfile_detail')
]