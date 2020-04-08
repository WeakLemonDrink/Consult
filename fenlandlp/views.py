from django.views import generic
from .models import Post, Comment
from accounts.models import Profile, Client
from .forms import CommentForm
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.core.files.storage import FileSystemStorage

class PostList(generic.ListView):
    queryset = Post.objects.select_related().filter(status=1).order_by("created_on")
    template_name = "index.html"
    paginate_by = 3

def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(request, request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.body = comment_form.cleaned_data['body']
            new_comment.user = request.user
            
            if comment_form.cleaned_data['file'] != None:
                new_comment.file = comment_form.cleaned_data['file']
                fs = FileSystemStorage()
                filename = fs.save(new_comment.file.name, new_comment.file)
                uploaded_file_url = fs.url(filename)
            
            new_comment.save()
             
    else:
        comment_form = CommentForm(request)

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


