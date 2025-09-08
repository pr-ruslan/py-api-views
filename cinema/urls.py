from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view({
        "get": "list",
        "post": "create"
    }), name="cinema-hall-list"),
    path("cinema_hall/<int:pk>/", CinemaHallDetail.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }), name="cinema-hall-detail"),
]

app_name = "cinema"
