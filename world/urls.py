from django.urls import path
from . import views
urlpatterns=[    
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('price',views.price,name='price'),
    path('blog',views.blog,name='blog'),
    path('detail',views.detail,name='detail'),
    path('team',views.team,name='team'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('appointment',views.appointment,name='appointment'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),


    
    
]