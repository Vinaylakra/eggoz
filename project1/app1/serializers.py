from rest_framework import serializers
from .models import Eggoz2


# class Eggoz2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Eggoz2
#         fields = (
#             "studentid",
#             "studentname",
#             "studentloc",
#             "studentphon",
#             "studentgen",
#             "addeddate",
#         )
        #  fields = "__all__"   or use like this 

class Eggoz2Serializer(serializers.Serializer):
          studentid = serializers.IntegerField(read_only = True)
          studentname = serializers.CharField(max_length = 50)
          studentloc = serializers.CharField(max_length = 100)
          studentphon = serializers.IntegerField()     
        #   studentphon = serializers.CharField(max_length=15)
          studentgen = serializers.CharField(max_length = 100)


          def create(self, validated_data):
                  return Eggoz2.objects.create(
                         studentname = validated_data['studentname'],
                         studentloc = validated_data['studentloc'],
                         studentphon = validated_data['studentphon'],
                         studentgen = validated_data['studentgen'],
                  )
          
          def update(self, instance, validated_data):
                  instance.studentname = validated_data.get('studentname', instance.studentname)
                  instance.studentloc = validated_data.get('studentloc', instance.studentloc)
                #   instance.studentphon = validated_data.get('studentphon', instance.studentphon)
                  instance.studentphon = validated_data.get('studentphon', instance.studentphon)
                  instance.studentgen = validated_data.get('studentgen', instance.studentgen)
                  instance.save()
                  return instance
          # for update .get is important this format is necessary 

