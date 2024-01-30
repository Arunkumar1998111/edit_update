from django.urls import path
from .views import home,logout_user,register_user,customer_record,delete_record, update_record,record_list




urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('record/<int:pk>',customer_record, name='record'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    # path('add_record/', add_record, name='add_record'),
    path('update_record/<int:pk>', update_record, name='update_record'),
    path('record_list/',record_list,name='record_list'),
    # path('edit/<int:pk>',edit_data,name="edit")
    
]
