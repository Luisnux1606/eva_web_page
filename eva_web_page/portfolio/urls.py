from django.urls import path
from . import views as portfolio_views

urlpatterns = [

    path('', portfolio_views.portfolio, name="portfolio"),
]



