"""Client_Rest_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # APP
    path('admin/', admin.site.urls),
    path('', include("client_frontend.urls")),
    path('api/', include(("client_API.urls", "API_URL_LINK"), namespace='api_url_link')),
    path('sign-in/', include('rest_framework.urls'), name='sign_in'),

    # # DJOSER TOKEN
    # path('auth/', include('djoser.urls')),
    # re_path('^auth-token/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/jwt', include('djoser.urls.jwt')),

    # JWT TOKEN
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
