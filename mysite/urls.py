"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import include, path

app_name = 'slash'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('slash/', views.index, name='index'),
    path('slash/bond/', views.buybond, name='bond'),
    path('slash/stock/', views.buystock, name='stock'),
    path('slash/stock/broker/apply/', views.applybroker, name='applybroker'),
    path('slash/stock/broker/save/', views.savebroker, name='savebroker'),
    path('slash/back/', views.back, name='back'),
    path('slash/credit/', views.credit, name='credit'),
    path('slash/credit/apply/', views.applycredit, name='applycredit'),
    path('slash/credit/save/', views.savecredit, name='savecredit'),
]
