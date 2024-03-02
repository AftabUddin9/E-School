from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('App_Login.urls')),
    path('', include('App_Articles.urls')),
    path('quizzes/', include('App_Quizzes.urls')),
    path('qna/', include('App_QnA.urls')),
]
