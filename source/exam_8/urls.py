"""exam_8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from webapp.views import ProductListView, ProductView, ProductCreate, Product_Update_View, Delete_Product, \
    ReviewCreateView, ReviewUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='title'),

    path('product/', include([
        path('<int:pk>/', include([
            path('', ProductView.as_view(), name='product_view'),
            path('update/', Product_Update_View.as_view(), name='update_product'),
            path('del/', Delete_Product.as_view(), name='del'),
            path('reviews/add/', ReviewCreateView.as_view(), name='review_add'),
            ])),


    path('product/add/', ProductCreate.as_view(), name='product_create'),

        path('review/', include([
            path('<int:pk>/', include([
                path('update/', ReviewUpdateView.as_view(), name='review_update'),
                # path('delete/', CommentDeleteView.as_view(), name='comment_delete'),
            ]))
        ]))
    ]))





]
