from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),

    path('update/<int:u_id>/', views.update, name="update"),    #<int:u_id>를 보낼 때 u_id부분은 views.py에서 update함수에서 pk에 넣어준 변수 이름으로 써줘야함!!!!!
    path('delete/<int:blog_id>/', views.delete, name="delete"), #delete부분도 마찮가지로 <int:blog_id>의 blog_id는 views.py에서 pk에 넣어준 변수이름임
]