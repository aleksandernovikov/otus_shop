from django import views

from blog.models import Post


class PostListView(views.generic.ListView):
    model = Post
    template_name = 'usability/'
