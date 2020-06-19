from django import views

from blog.models import Post, PostCategory


class BlogRootListView(views.generic.ListView):
    model = Post
    template_name = 'usability/pages/blog.html'


class BlogCategoryListView(views.generic.ListView):
    model = Post
    template_name = 'usability/pages/blog.html'
    paginate_by = 6

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return self.model.objects.filter(category__slug=category_slug)


class BlogPostView(views.generic.DetailView):
    model = Post
    template_name = 'usability/pages/post.html'
