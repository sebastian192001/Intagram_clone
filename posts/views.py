#Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
#Model
from posts.models import Post
#Forms
from posts.forms import PostForm





class PostsFeedView(LoginRequiredMixin, ListView):
    """return all published posts"""

    template_name = "posts/feed.html"
    model = Post
    ordering = ("-create",)
    paginate_by = 30
    context_object_name = "posts"

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = "posts/new.html"

    form_class = PostForm

    success_url = reverse_lazy("posts:feed")

    def get_context_data(self, **kwargs):
        """add user and profile to contex"""
        context = super().get_context_data(**kwargs)
        context ["user"] = self.request.user
        context ["profile"] = self.request.user.profile
        return context


