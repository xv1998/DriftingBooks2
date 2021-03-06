"""driftingbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url

import Order.views as orderviews

urlpatterns = [
    path('fill_receive_order/', orderviews.fill_receive_order, name='fill_receive_order'),
    path('fill_retrive_order/', orderviews.fill_retrive_order, name='fill_retrive_order'),
    path('fill_acquire_order/', orderviews.fill_acquire_order, name='fill_acquire_order'),
    path('accept_book_order/', orderviews.accept_book_order, name='accept_book_order'),
    path('reject_book_order/', orderviews.reject_book_order, name='reject_book_order'),
    path('reject_book_order/', orderviews.reject_book_order, name='reject_book_order'),
    path('retrive_book/', orderviews.retrive_book, name='retrive_book'),
    path('get_order/', orderviews.get_order, name='get_order'),
    path('get_orders_of_user/', orderviews.get_orders_of_user, name='get_orders_of_user'),    
]
