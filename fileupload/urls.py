from django.urls import path
from .views import register,login_view, upload, download, prevupload
from django.contrib.auth import views 

urlpatterns = [
    path('', register, name="register"),
    path('upload/', upload, name="upload"),
    path('prevupload/', prevupload, name="prevupload"),
    path('download/', download, name="download"),
    path('login/', login_view, name="login"),
    path('logout/', views.LogoutView.as_view(template_name='fileupload/logout.html'), name="logout"),
]    