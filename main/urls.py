from django.urls import path
from main.views import show_main, register_product, show_xml, show_json, show_xml_by_id, show_json_by_id
#TUGAS 4
from main.views import register
from main.views import login_user
from main.views import logout_user

from main.views import logout_user
from main.views import delete_product
from main.views import edit_product

#TUGAS 6
from main.views import add_product_entry_ajax

#TUGAS 6
from main.views import create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register-product', register_product, name='register_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    #TUGAS 4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #TUGAS 5
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    


]