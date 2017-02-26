"""Defines URLs for learning_logS"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    url(r'^topics/(?P<slug>[-\w]+)/$', views.topic_by_slug, name='topic_by_slug'),

    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # category test (3rd param name = unique name for url)
    url(r'^category1/(\w+)/(\w+)/$', views.get_category1, name='category1'),

    # this is the same as above, but vars used as placeholders
    url(r'^category2/(?P<category>\w+)/(?P<subcategory>\w+)/$', views.get_category2, name='category2'),

]