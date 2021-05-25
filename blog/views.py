from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth import get_user_model


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'
    

class BlogDetailView(LoginRequiredMixin, DetailView):

    
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all
        return context


class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body', 'author',)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('__all__')