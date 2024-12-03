from django.shortcuts import render,redirect
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.
from .serializers import Eggoz2Serializer
from .models import Eggoz2
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView 

from rest_framework import mixins, generics
from rest_framework import status
from django.http import Http404
from rest_framework.viewsets import ViewSet

  # they are example of generic  API view 
# class EggozCreate(CreateAPIView):
#     queryset = Eggoz2.objects.all()
#     serializer_class = Eggoz2Serializer


# class EggozList(ListAPIView):
#     queryset = Eggoz2.objects.all()
#     serializer_class = Eggoz2Serializer

# class EggozRetrieve(RetrieveAPIView):
#     queryset = Eggoz2.objects.all()
#     serializer_class = Eggoz2Serializer


# class EggozDestroy(DestroyAPIView):
#     queryset = Eggoz2.objects.all()
#     serializer_class = Eggoz2Serializer

# class EggozUpdate(UpdateAPIView):
#     queryset = Eggoz2.objects.all()
#     serializer_class = Eggoz2Serializer


#exapmle of customized api view
class EggozCreate(CreateAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer
    def create(self, request, *args, **kwargs):
        eggoz = Eggoz2.objects.create(
            studentname = request.data['studentname'],
            studentloc = request.data['studentloc'],
            studentphon = request.data['studentphon'],
            studentgen = request.data['studentgen'],
        )
        serializer = Eggoz2Serializer(eggoz)

        return Response(serializer.data)
    

class EggozList(ListAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer

    def get(self, request, *args, **kwargs):
        eggoz = Eggoz2.objects.all()

        serializer = Eggoz2Serializer(eggoz, many = True)
        return Response(serializer.data)
    

class EggozRetrieve(RetrieveAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer

    def retrieve(self, request, *args, **kwargs):
        eggoz = Eggoz2.objects.get(studentid = kwargs['studentid'])

        serializer = Eggoz2Serializer(eggoz)
        return Response(serializer.data)
    
class EggozDestroy(DestroyAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer

    def destroy(self, request, *args, **kwargs):
        try:
            eggoz = Eggoz2.objects.get(studentid = kwargs['studentid'])
            eggoz.delete()
        except:
            return Response('ID does not exist !!!')
        
        return Response('====Deletion Completed====') 
    
class EggozUpdate(UpdateAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer

    def update(self, request, *args, **kwargs):
        try:
            eggoz = Eggoz2.objects.get(studentid = kwargs['studentid'])
            eggoz.studentname = request.data.get('studentname')
            eggoz.studentloc = request.data.get('studentloc')
            eggoz.studentphon = request.data.get('studentphon')
            eggoz.studentgen = request.data.get('studentgen')
            eggoz.save()

            serializer = Eggoz2Serializer(eggoz)
            return Response(serializer.data)
        
        except:
            return Response('Cant Update it !!!!!!!')

        return Response('Updated Successfully')


#---------------------------------------------------------------------------------------------------------------
# use postman to access features 
class EggozView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = Eggoz2Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "post method called successfully!"},serializer.data)
    
        return Response(serializer.errors)
    

    def get(self, request, *args, **kwargs):
        queryset = Eggoz2.objects.all()
        serialzer = Eggoz2Serializer(queryset, many = True)
        return Response({"message": "GET method called successfully!"},serialzer.data)
    
    def put(self, request, *args, **kwargs):
        return Response({"message": "put method called successfully!"})
    
    def patch(self, request, *args, **kwargs):
        return Response({"message": "patch method called successfully!"})
   
    def delete(self, request, *args, **kwargs):
        return Response({"message": "delete method called successfully!"})
    

#----------------------------------------------------------------------------------------------------------------

class EggozMixinsView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Eggoz2.objects.all()
    serializer_class = Eggoz2Serializer

    def get(self, request, *args, **kwargs):

        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
         return self.partial_update(request, *args, **kwargs)
    #     response = self.partial_update(request, *args, **kwargs)  # Perform the partial update
    #     return Response(
    #     {
    #         "message": "Object updated successfully!",
    #         "data": response.data  # Include updated data
    #     },
    #  )


    def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)   # it is working alone method 2
        instance = self.get_object()  # Retrieve the object to delete
        self.perform_destroy(instance)  # Delete the object
        return Response({"message": "Object deleted successfully!"})
    


#---------------------------------------------------------Viewset example--------------------------------------
# make sure to uncomment urls from project folder the commented part 
class EggozViewset(ViewSet):
    #http://127.0.0.1:8000/api/models/ us ethis format to call this
    def list(self, request):
        models = Eggoz2.objects.all()
        serializer = Eggoz2Serializer(models, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        try:
            models = Eggoz2.objects.get(pk = pk)
        except Eggoz2.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = Eggoz2Serializer(models)
        return Response(serializer.data)
        
    def create(self, request):
            serializer = Eggoz2Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def destroy(self ,request, pk = None):
        try:
            models = Eggoz2.objects.get(pk = pk)
            models.delete()
            return Response("Deleted successfully!!")
        except Eggoz2.DoesNotExist:
            return Response("Does Not Exist")
        
    # in url http://127.0.0.1:8000/api/models/<pk>/ use this format  for delete and update and for particular access
    def update(self, request, pk = None):
        model = Eggoz2.objects.get(pk = pk)
        serializer = Eggoz2Serializer(model, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)