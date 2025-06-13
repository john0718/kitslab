"""
URL configuration for kits_labsemster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include('kitslab.urls')),
    path('', include('authentication.urls')),
    path('faculty/', include('faculty.urls')),
    path('time/', include('ctc_examtime.urls')),
    path('ctc_home/',include('ctc_home.urls')),
    path('ctc_seraphauthentication/',include('ctc_seraphauthentication.urls')),
    path('GCRdraft/',include('GCR_draft.urls',namespace='gcr_draft')),

]
