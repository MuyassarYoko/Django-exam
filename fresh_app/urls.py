from django.urls import path

from fresh_app.views import EventList, EventDetail, CategoryList, CategoryDetail, CommentList, FavouriteList, \
    CategoryCreate, EventCreate, CategoryUpdate, CategoryDelete, CommentDUD, FavouriteDUD, EventUpdate, EventDelete

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/create/', EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>', EventDetail.as_view(), name='event-detail'),
    path('events/update/<int:pk>', EventUpdate.as_view(), name='event-update'),
    path('events/delete/<int:pk>', EventDelete.as_view(), name='event-delete'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/create/', CategoryCreate.as_view(), name='category-create'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('categories/update/<int:pk>', CategoryUpdate.as_view(), name='category-update'),
    path('categories/delete/<int:pk>', CategoryDelete.as_view(), name='category-delete'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('comments/<int:pk>', CommentDUD.as_view(), name='comment-dud'),
    path('favorite/', FavouriteList.as_view(), name='favorite-detail'),
    path('favorite/<int:pk>', FavouriteDUD.as_view(), name='favorite-dud')
]
