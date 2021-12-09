from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# VIEWS

'''
test posts
posts = [
    {
        'author': 'Joe123',
        'title': 'first forum post',
        'content': 'first post content',
        'date_posted': 'December 1, 2021'
    },
    {
        'author': 'CatLover2',
        'title': 'second forum post',
        'content': 'second post content',
        'date_posted': 'December 2, 2021'
    },
]
'''
# home page
def home(request):
    # Load template
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'forum/home.html', context)

'''
Loads the test posts
def home(request):
    # Load template
    context = {
        'posts': posts
    }
    return render(request, 'forum/home.html', context)
'''

def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})

# class based views
class PostListView(ListView):
    model = Post
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    # the minus makes it newest first
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #  to see if user is owner of post before update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    #  to see if user is owner of post before delete
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False