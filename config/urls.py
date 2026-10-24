from django.urls import include, path

urlpatterns = [
    path("api/", include("saludo.infrastructure.web.urls")),
]
