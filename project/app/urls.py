from django.urls import path , include
from app import views
urlpatterns = [
    path('latest_products/',views.LatestProductList.as_view(),name='products-list'),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view() , name='product-details'),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view(),name='category-details'),
    path('products/search/',views.search,name='product-search'),



]   
