from django import views
from django.http import Http404

from blog.models import Post, PostCategory


class BlogMixin:
    paginate_by = 4


class BlogRootListView(BlogMixin, views.generic.ListView):
    model = Post
    template_name = 'usability/pages/blog.html'


class BlogCategoryListView(BlogMixin, views.generic.ListView):
    model = Post
    template_name = 'usability/pages/blog.html'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return self.model.objects.filter(category__slug=category_slug)

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        try:
            ctx.update({
                'category': PostCategory.objects.get(slug=self.kwargs.get('slug'))
            })
        except PostCategory.DoesNotExist:
            raise Http404

        return ctx


class BlogPostView(views.generic.DetailView):
    model = Post
    template_name = 'usability/pages/post.html'
