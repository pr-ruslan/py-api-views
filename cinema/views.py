from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin
)
from rest_framework import status

from django.shortcuts import get_object_or_404

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall
)

from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class GenreList(APIView):
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_genre_obj(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk, format=None):
        serializer = GenreSerializer(self.get_genre_obj(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = GenreSerializer(self.get_genre_obj(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_genre_obj(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(ListModelMixin,
                CreateModelMixin,
                GenericAPIView,
                ):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetail(RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CinemaHallList(
        ListModelMixin,
        CreateModelMixin,
        GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class CinemaHallDetail(
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer





# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#
#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "PUT":
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
