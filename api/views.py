from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes  # two decoraters for authentication and permission
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication                           # For authentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions       # For Permission
from .custompermissions import myperm
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])

# @authentication_classes([BasicAuthentication])
# @authentication_classes([SessionAuthentication])
# @authentication_classes([CustomAuthentication])
# @authentication_classes([TokenAuthentication])
@authentication_classes([JWTAuthentication])                  #JWT authenticaation

# # @permission_classes([AllowAny])                           # Anyone can access the api
# # @permission_classes([IsAdminUser])                        # Only staff user can access
@permission_classes([IsAuthenticated])                    # All authenticated user can access
# # @permission_classes([IsAuthenticatedOrReadOnly])          # all access to authenticated users but read only for anyonyoumus users
# # @permission_classes([DjangoModelPermissions])             # ??????
# @permission_classes([myperm])                               # For custom permissions

def student_api(request,pk=None):

    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'})
        return Response(serializer.errors)


    if request.method == 'PATCH':
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})        

















# #            Testing by browseable api



# @api_view(['GET','POST','PUT','PATCH','DELETE'])

# # @authentication_classes([BasicAuthentication])
# # @authentication_classes([SessionAuthentication])

# # # @permission_classes([AllowAny])                           # Anyone can access the api
# # # @permission_classes([IsAdminUser])                        # Only staff user can access
# # # @permission_classes([IsAuthenticated])                    # All authenticated user can access
# # # @permission_classes([IsAuthenticatedOrReadOnly])          # all access to authenticated users but read only for anyonyoumus users
# # # @permission_classes([DjangoModelPermissions])             # ??????
# # @permission_classes([myperm])                               # For custom permissions

# def student_api(request,pk=None):

#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'PUT':
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'PATCH':
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})        

















# if we use a 3rd party application for testing thaan we use this function

# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)


#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated'})
#         return Response(serializer.errors)


#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})        
