from bson import ObjectId
from school.models import School
from school.serializator import SchoolSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


class SchoolListView(APIView):
    """
    View class for listing all, and creating a new schools, endpoint: /school/
    """
    def get(self, request) -> Response:
        """For listing out the schools, HTTP method: GET"""
        schools = School.objects.all()
        # Passing the queryset through the serializer
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        """For creating a new School, HTTP method: POST"""

        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolDetailView(APIView):
    """
    View class for listing, updating and deleting a single school,
    endpoint: /schools/<str:_id>/
    """


    def get(self, request, _id: str = None) -> Response:
        """For listing out a single school, HTTP method: GET"""

        school = get_object_or_404(School, pk=ObjectId(_id))
        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, _id: str = None):
        """For updating an existing school, HTTP method: PUT"""
        school = get_object_or_404(School, pk=ObjectId(_id))
        serializer = SchoolSerializer(school, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id: str = None) -> Response:
        """For deleting a school, HTTP method: DELETE"""
        school = get_object_or_404(School, pk=ObjectId(_id))
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

