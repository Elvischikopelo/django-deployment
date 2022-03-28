from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import  generic 
from .models import Comment,Post 
from .forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutView(generic.TemplateView):
    template_name ='about.html'

class PostListView(generic.ListView):
    model = Post 

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class DraftListView(generic.ListView):
    model =Post 

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


class PostCreate(LoginRequiredMixin,generic.CreateView):
    model = Post
    form_class = PostForm 
    template_name =' post_create.html'

class PostDetail(generic.DetailView):
    model = Post 

class PostUpdate(LoginRequiredMixin,generic.UpdateView):
    model =Post
    form_class = PostForm


class DeletePost(LoginRequiredMixin,generic.DeleteView):
    model =Post 
    success_url = reverse_lazy('posts:all')



@login_required 
def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        form =CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =post 
            comment.save()
            return redirect('posts:detail',pk=post.pk)
    else:
        form =CommentForm()
    return render(request,'posts/comment_form.html',{'form':form})


@login_required 
def comment_approve(request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('posts:detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk =comment.post.pk 
    comment.delete()
    return redirect('posts:detail',pk=post_pk)


@login_required 
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()

    return redirect('posts:detail',pk=post.pk)