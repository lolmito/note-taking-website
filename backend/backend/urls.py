from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView #once the user is created we can use the pre-built views to obtain the tokens to sign them in 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #Prebuilt views to first get access and refresh tokens and second refresh the tokens


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/',CreateUserView.as_view(), name="register"),
    path('api/token/',TokenObtainPairView.as_view(), name="get_token"),
    path('api/token/refresh',TokenRefreshView.as_view(), name="refresh_token"),
    path('api-auth/', include("rest_framework.urls")),
    path('api/',include("api.urls")), # if the url is "api/" then go to api.urls file to parse the remaining part of the url
]
