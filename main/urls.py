from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact-us',views.contactus,name='contactus'),
    path('about-us',views.aboutus,name='aboutus'),
    path('blog',views.blog,name='blog'),
    path('smartphones',views.smartphones,name='smartphones'),
    path('laptops',views.laptops,name='laptops'),
    path('wearables',views.wearables,name='wearables'),
    path('blog1',views.blog1,name='blog1'),
    path('blog2',views.blog2,name='blog2'),
    path('Buy/<str:product_name>/<int:price>/',views.Buyfunction,name='Buy')
    
]
