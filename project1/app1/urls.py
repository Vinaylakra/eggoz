from django.urls import path
from .views import EggozCreate,EggozDestroy,EggozList,EggozRetrieve,EggozUpdate,EggozView
from .views import EggozMixinsView
urlpatterns = [

    path("eggoz/create/", EggozCreate.as_view(), name="eggoz_create"),

    # path("eggoz/destroy/<int:pk>", EggozDestroy.as_view(), name="eggoz_Destroy"),
    path("eggoz/destroy/<int:studentid>", EggozDestroy.as_view(), name="eggoz_Destroy"),

    path("eggoz/list/", EggozList.as_view(), name="eggoz_List"),

    # path("eggoz/retrieve/<int:pk>", EggozRetrieve.as_view(), name="eggoz_Retrieve"),
    path("eggoz/Retrieve/<int:studentid>", EggozRetrieve.as_view(), name="eggoz_Retrieve"),

    # path("eggoz/update/<int:pk>", EggozUpdate.as_view(), name="eggoz_Update"),   
    path("eggoz/update/<int:studentid>", EggozUpdate.as_view(), name="eggoz_Update"), 


    path("eggoz/", EggozView.as_view(), name="eggoz_view"),


     #for mixins
     #URL for listiing all objects and creating a new objects(getpost)
     path('eggoz/mixins/', EggozMixinsView.as_view(), name='eggoz_list_create'),
     
     #URl for retriving,update,delet specific 
     path('eggoz/mixins/<int:pk>', EggozMixinsView.as_view(), name='eggoz_details'),

]
