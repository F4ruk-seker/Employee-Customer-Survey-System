from django.urls import path, include

app_name = "api"

urlpatterns = [
    path('', include('pars_auth.api.urls', namespace="auth_api")),
    path('exam/', include('anket.api.urls', namespace="exam_api")),
]

