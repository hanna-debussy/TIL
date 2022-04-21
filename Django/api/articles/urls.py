from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # GET => index / POST => create
    path("", views.article_index_create),
    
    # GET => detail / PUT => update / DELETE => delete
    path("<int:article_pk>/", views.article_detail_update_delete),

    # POST => create comment
    path("<int:article_pk>/comments/", views.comment_create),

    # PUT => update comment / DELETE => delete comment
    path("<int:article_pk>/comments/<int:comment_pk>/", views.comment_update_delete),
]
