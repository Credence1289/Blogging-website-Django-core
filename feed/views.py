from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, 'blog-temp/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog-temp/home.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']

class UserPostListView(ListView):
    model = Post
    template_name = 'blog-temp/user-post-list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_on')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog-temp/post-detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog-temp/post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog-temp/post-update.html'
    fields = ['title', 'content']
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog-temp/post-delete.html'
    success_url = '/'
    pk_url_kwarg = 'id'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request, 'blog-temp/about.html')

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query) if query else Post.objects.none()
    return render(request, 'blog-temp/search.html', {'results': results, 'query': query})







