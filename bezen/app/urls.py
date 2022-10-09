from django.urls import path
from .views import Index
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',Index.as_view(),name="index"),

    path('createrecipe',views.UploadRecipe.as_view(),name="uploadrecipe"),
    path('editrecipe/<int:id>',views.EditRecipe.as_view(),name="editrecipe"),
    path('deleterecipe/<int:id>',views.DeleteRecipe.as_view(),name='deleterecipe'),
    path('viewrecipe/<int:id>/',views.Recipe.as_view(),name="viewrecipe"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)