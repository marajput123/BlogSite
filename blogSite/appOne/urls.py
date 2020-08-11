from django.conf.urls import url
from . import views

app_name = 'appOne'

urlpatterns = [
    url(r'^$',views.PostListView.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)/$',views.PostDetailView.as_view(), name = 'detail' ),
    url(r'^(?P<pk>\d+)/create_com/$',views.add_comment_to_post, name = 'create_comment' ),
    url(r'^post_form/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^my_blog/$',views.PostMyBlogView.as_view(), name = 'myblog'),
    url(r'^my_blog/(?P<pk>\d+)/$',views.my_blog_detail, name = 'my_blog_detail' ),
    url(r'^my_blog/\d+/(?P<pk>\d+)/$',views.comment_delete, name = 'comment_delete'),
    url(r'^my_blog/delete/(?P<pk>\d+)/$',views.PostMyBlogDelete.as_view(), name = 'delete'),
    url(r'^draft/$',views.PostMyDraftView.as_view(), name = 'draft'),
    url(r'^draft/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name = 'update'),
    url(r'^draft/(?P<pk>\d+)/publish/$', views.publish, name = 'publish'),
    # Creating a blog is linked to the url below


]
