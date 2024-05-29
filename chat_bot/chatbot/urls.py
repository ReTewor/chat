from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('information__about__bot.html', TemplateView.as_view(template_name='information__about__bot.html'), name='information__about__bot'),
    path('examples__of__dialogs.html', TemplateView.as_view(template_name='examples__of__dialogs.html'), name='examples__of__dialogs'),
    #path('home.html', TemplateView.as_view(template_name='home.html'), name='home'),
]
