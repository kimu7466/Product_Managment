from django.urls import path
from . import views 

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('manager_login/', views.manager_login, name='manager_login'),
    path('log_out/', views.log_out, name='log_out'),
    path('add_product_name/', views.add_product_name, name='add_product_name'),
    path('product_detail/<int:p_id>', views.product_detail, name='product_detail'),
    path('show_details_view/', views.show_details_view, name='show_details_view'),
    path('update_detail/<int:id>', views.update_detail, name='update_detail'),
    path('delete_detail/<int:id>', views.delete_detail, name='delete_detail'),
    path('update_name/<int:p_id>', views.update_name, name='update_name'),
    path('delete_name/<int:p_id>', views.delete_name, name='delete_name'),
    path('search/',views.product_search, name='product_search'),
    
    # path('product_list/', views.product_list, name='product_list'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # Add URL patterns for adding, updating, and deleting products
    # path('search/', views.search, name='search'),
]
