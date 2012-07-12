#from django.conf.urls import *
                                #start base
#urlpatterns = patterns('',)

from django.conf.urls import *
                               
urlpatterns = patterns('',
url(r'^post/search/(\w+)','blog.views.post_search'),
url(r'^posts/$', 'blog.views.post_list'),
url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),  
)
