from django.urls import path
from . import views
from .views import BooksProfile, IndexView, BooksAdd, BooksFollow, BooksUnfollow, BooksDetail, BooksDestroy

app_name = "books"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('books', BooksAdd.as_view(), name="books"),
    path('books/profile', BooksProfile.as_view(), name="profile"),
    path('books/<int:pk>', BooksDetail.as_view(), name="detail"),
    path('books/<int:pk>/follow', BooksFollow.as_view(), name="follow"),
    path('books/<int:pk>/unfollow', BooksUnfollow.as_view(), name="unfollow"),
    path('books/<int:pk>/destroy', BooksDestroy.as_view(), name="destroy"),
]
