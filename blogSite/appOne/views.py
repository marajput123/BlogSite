from django.shortcuts import render, get_object_or_404, redirect
from appOne.forms import UserForm, CommentForm, PostForm
from appOne.models import Post,Comment,User
from django.utils import timezone

from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView,ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,
                                    RedirectView)
# Create your views here.

class PostListView(ListView):
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(create_date__lte=timezone.now(), is_published=True).order_by('-publish_date')

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = Post
    template_name = 'appOne/post_detail.html'

class PostCreate(LoginRequiredMixin,CreateView):
    login_url = '/user_login/'
    redirect_field_name = 'appOne/myblog.html'
    form_class = PostForm
    model = Post


    def form_valid(self, form):
        post = form.save(commit = False)
        post.user = self.request.user
        post.save()
        return redirect('appOne:myblog')
        # return super(PostCreate, self).form_valid(form)

class PostMyBlogView(LoginRequiredMixin,ListView):
    login_url = '/user_login/'
    redirect_field_name = 'appOne/myblog.html'
    context_object_name = 'myblog_list'
    model = Post
    template_name = 'appOne/my_blog.html'
    def get_queryset(self):
        return Post.objects.filter(user__id=self.request.user.id).order_by('-create_date')

class PostMyBlogDelete(LoginRequiredMixin, DeleteView):
    context_object_name = 'post'
    model = Post
    success_url = reverse_lazy('appOne:myblog')

class PostMyDraftView(LoginRequiredMixin, ListView):
    login_url = '/user_login/'
    redirect_field_name = 'appOne/myblog.html'
    context_object_name = 'draft_list'
    model = Post
    template_name = 'appOne/drafts.html'
    def get_queryset(self):
        return Post.objects.filter(user__id=self.request.user.id, is_published=False).order_by('-create_date')

class DrafDetailView(LoginRequiredMixin,DetailView):
    login_url = '/user_login/'
    redirect_field_name = 'appOne/draft.html'
    context_object_name = 'draft_detail'
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/user_login/'
    redirect_field_name = 'appOne/draft.html'
    context_object_name = 'form'
    form_class = PostForm
    model = Post
    template_name = 'appOne/post_update.html'
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.save()
        return redirect('appOne:draft')












def register(request):

    is_registered = False
    forms = UserForm()

    if request.method == "POST":
        user_info = UserForm(data = request.POST)

        if user_info.is_valid():

            user = user_info.save()
            user.set_password(user.password)
            user.save()

            is_registered = True

        else:
            print(user_info.errors)



    return render(request,"registration.html",{'forms':forms,
                                                 'is_registered':is_registered})

def userlogin_main(request):

    is_incorrect = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            is_incorrect = False
            return HttpResponseRedirect(reverse('homepage'))

        else:
            is_incorrect = True

    return render(request, 'homepage.html', {'is_incorrect': is_incorrect})

def user_login(request):

    is_incorrect = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('homepage')
            is_incorrect = False

        else:

            is_incorrect = True

    return render(request, 'login.html', {'is_incorrect':is_incorrect})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.author = '{} {}'.format(request.user.first_name, request.user.last_name)
            comment.save()

            return redirect('appOne:detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'appOne/comment_form.html',{'form':form})

@login_required
def my_blog_detail(request,pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request,'appOne/my_blog_detail.html', {'post_detail':post_detail})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('appOne:my_blog_detail',pk=post_pk)

@login_required
def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('appOne:myblog')
