from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView,BlockView,check,MODProfileListView
from users.views import ReportView 

urlpatterns = [
    path('',views.home,name = 'meet-home'),
    path('profile/new/',ProfileCreateView.as_view(),name = 'profile-create'),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name = 'profile-detail'),
    path('<int:pk>/accepted',views.accepted,name = 'accepted'),
    path('profile/<int:pk>/update/',ProfileUpdateView.as_view(),name = 'profile-update'),  # meet-home used in template particularly css file
    path('about/',views.about,name = 'meet-about'),
    path('req_to_chat',views.req_to_chat,name ='meet-chat'),
    path('block/unblock',views.unblock,name ='unblock'),
    path('profile/block_user',views.block_user,name ='meet-block'),
    path('profile/new/',ProfileCreateView.as_view(),name = 'profile-create'),
    path('report/',ReportView.as_view(),name = 'profile-report'),
    path('message/send',views.send,name= 'send'),
    path('chat/',views.chat,name= 'chat'),
    path('chat/chat/<str:room>/',views.room,name = 'room'),
    path('chat/checkview',views.check,name = 'check'),
    path('block/',BlockView.as_view(),name = 'profile-block'),
    path('ShowMessages/<str:room>/',views.ShowMessages,name = 'ShowMessages'),
    # path('UnreadMessages/<str:room>/',views.UnreadMessages,name = 'UnreadMessages'),
    path('search/',views.search,name = 'search'),
    path('modprofile/', MODProfileListView.as_view(),name = 'modprofile'),
    path('username/', views.update_username ,name = 'update_username'),

]