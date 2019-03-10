from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from xml_score import views


urlpatterns = [
    path('create/', views.XmlScoreCreateView.as_view(), name='create'),
    path('detail-view/<pk>/', views.XmlScoreDetailView.as_view(), name='detail-view'),
    path('xml-score/<pk>/', views.XmlScoreView.as_view(), name='calculated-score'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)