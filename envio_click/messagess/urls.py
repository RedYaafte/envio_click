from django.urls import path

from messagess import views

urlpatterns = [
    path('<pk>/', views.MessageDetailView.as_view(), name='message-detail'),
    path('decipher/<pk>/', views.MessageDecipherView.as_view(), name='decipher'),
]