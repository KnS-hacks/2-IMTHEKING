from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload, name="upload"),
    path('main/', main, name="main"),
    path('selectlocation/<int:Concert_id>/', location, name="selectlocation"),
    path('update/<int:Concert_id>/', update, name="update"), # 수정됨
    path('detail/<int:Concert_id>/', detail, name="detail"), #수정됨
    path('delete/<int:Concert_id>/', delete, name="delete"), #수정됨
]