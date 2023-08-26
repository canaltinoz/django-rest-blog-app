from django.urls import path,include
from account.api.views import ProfileView

app_name='account'
urlpatterns = [
    path('me/',ProfileView.as_view(),name='me'),


]
